"""
Hermes-Paperclip Bridge
Paperclip organizasyonlarını Hermes agent'ina baglar.
"""

import json
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx
import yaml


@dataclass
class AgentRole:
    role: str
    label: str
    skills: list[str] = field(default_factory=list)
    max_concurrent_runs: int = 5
    budget_limit_cents: int = 0


@dataclass
class Organization:
    name: str
    prefix: str
    roles: list[AgentRole] = field(default_factory=list)
    telegram_bot_token: str = ""
    telegram_allowed_users: list[int] = field(default_factory=list)


@dataclass
class BridgeConfig:
    hermes_api_url: str = "http://localhost:8642/v1"
    paperclip_api_url: str = "http://localhost:3100"
    locale: str = "tr"
    organizations: list[Organization] = field(default_factory=list)
    skills_source: str = ""
    cron_jobs: list[dict[str, Any]] = field(default_factory=list)


def load_config(path: str = "config.yaml") -> BridgeConfig:
    config_path = Path(__file__).parent / path
    with open(config_path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    bridge = raw.get("bridge", {})
    cfg = BridgeConfig(
        hermes_api_url=bridge.get("hermes_api_url", "http://localhost:8642/v1"),
        paperclip_api_url=bridge.get("paperclip_api_url", "http://localhost:3100"),
        locale=raw.get("locale", "tr"),
        skills_source=raw.get("skills_source", ""),
        cron_jobs=raw.get("cron", []),
    )

    for org_data in raw.get("organizations", []):
        if org_data.get("name") == "":
            continue
        roles = []
        for r in org_data.get("roles", []):
            roles.append(AgentRole(
                role=r["role"],
                label=r["label"],
                skills=r.get("skills", []),
                max_concurrent_runs=r.get("max_concurrent_runs", 5),
                budget_limit_cents=r.get("budget_limit_cents", 0),
            ))
        cfg.organizations.append(Organization(
            name=org_data["name"],
            prefix=org_data["prefix"],
            roles=roles,
        ))

    return cfg


class HermesClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(timeout=60.0)

    def chat(self, message: str, session_id: str | None = None) -> dict:
        payload: dict[str, Any] = {
            "model": "hermes-agent",
            "messages": [{"role": "user", "content": message}],
        }
        if session_id:
            payload["session_id"] = session_id

        resp = self.client.post(
            f"{self.base_url}/chat/completions",
            json=payload,
        )
        resp.raise_for_status()
        return resp.json()

    def health(self) -> bool:
        try:
            resp = self.client.get(f"{self.base_url}/models")
            return resp.status_code == 200
        except httpx.ConnectError:
            return False


class PaperclipClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(timeout=30.0)

    def health(self) -> bool:
        try:
            resp = self.client.get(f"{self.base_url}/health")
            return resp.status_code == 200
        except httpx.ConnectError:
            return False

    def create_organization(self, name: str, prefix: str) -> dict | None:
        try:
            resp = self.client.post(
                f"{self.base_url}/api/companies",
                json={"name": name, "issuePrefix": prefix.upper()},
            )
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPError as e:
            print(f"  [HATA] Organizasyon olusturulamadi: {e}")
            return None

    def create_agent(self, company_id: str, role_config: AgentRole) -> dict | None:
        try:
            resp = self.client.post(
                f"{self.base_url}/api/companies/{company_id}/agents",
                json={
                    "name": role_config.label,
                    "role": role_config.role,
                    "adapterType": "http",
                    "maxConcurrentRuns": role_config.max_concurrent_runs,
                    "config": {
                        "endpoint": "http://localhost:8642/v1/chat/completions",
                        "skills": role_config.skills,
                    },
                },
            )
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPError as e:
            print(f"  [HATA] Ajan olusturulamadi ({role_config.label}): {e}")
            return None


def load_skills(skills_dir: str) -> dict[str, str]:
    skills = {}
    base = Path(skills_dir)
    if not base.exists():
        print(f"  [UYARI] Skill dizini bulunamadi: {skills_dir}")
        return skills

    for skill_file in base.rglob("SKILL.md"):
        skill_name = skill_file.parent.name
        skills[skill_name] = str(skill_file)
    return skills


def setup_organization(
    paperclip: PaperclipClient,
    hermes: HermesClient,
    org: Organization,
) -> bool:
    print(f"\n=== Organizasyon: {org.name} ===")

    org_data = paperclip.create_organization(org.name, org.prefix)
    if not org_data:
        return False

    company_id = org_data.get("id", "")
    print(f"  [OK] Organizasyon olusturuldu (ID: {company_id})")

    for role_config in org.roles:
        agent = paperclip.create_agent(company_id, role_config)
        if agent:
            print(f"  [OK] Ajan: {role_config.label} ({role_config.role})")
            print(f"       Skill'ler: {', '.join(role_config.skills)}")
        else:
            print(f"  [SKIP] Ajan: {role_config.label}")

    return True


def check_health(hermes: HermesClient, paperclip: PaperclipClient) -> bool:
    print("=== Saglik Kontrolu ===")

    h = hermes.health()
    p = paperclip.health()

    print(f"  Hermes API:     {'AKTIF' if h else 'PASIF'} ({hermes.base_url})")
    print(f"  Paperclip API:  {'AKTIF' if p else 'PASIF'} ({paperclip.base_url})")

    if not h:
        print("\n  [HATA] Hermes API'ye erisilemiyor.")
        print("  Hermes'i baslat: hermes gateway veya python run_agent.py")
    if not p:
        print("\n  [HATA] Paperclip API'ye erisilemiyor.")
        print("  Paperclip'i baslat: paperclipai run")

    return h and p


def main():
    config = load_config()
    print("=== Hermes-Paperclip Bridge ===")
    print(f"  Dil: {config.locale}")
    print(f"  Skill kaynagi: {config.skills_source or 'yok'}")

    hermes = HermesClient(config.hermes_api_url)
    paperclip = PaperclipClient(config.paperclip_api_url)

    if not check_health(hermes, paperclip):
        print("\nHer iki servis de calismali. Cikiliyor.")
        sys.exit(1)

    if config.skills_source:
        skills = load_skills(config.skills_source)
        print(f"\n  [OK] {len(skills)} skill yuklendi")

    if not config.organizations:
        print("\n  [INFO] Henuz musteri organizasyonu yok.")
        print("  config.yaml dosyasina musteri ekleyin.")
        return

    for org in config.organizations:
        setup_organization(paperclip, hermes, org)

    print("\n=== Tamamlandi ===")


if __name__ == "__main__":
    main()
