---
title: VPS Deployment Stratejisi
tags: [decision, deployment, vps, docker, coolify, github]
source: repo/Dockerfile, repo/docker/entrypoint.sh
date: 2026-04-22
status: active
brain: A
---

# Karar: VPS Deployment Stratejisi

## Baglam

Hermes Agent v0.10.0 Windows'da calisiyor ama production icin VPS gerekli.
Dockerfile hazir, entrypoint scripti mevcut. **VPS'te Coolify kurulu.**

## Karar

**GitHub → Coolify** (self-hosted PaaS uzerinden konteyner deploy)

```
Local → GitHub private repo → Coolify auto-pull → Docker build → Container
```

## Neden Coolify

Coolify self-hosted bir PaaS (Heroku/Vercel benzeri):
- Web UI'dan GitHub repo bagla, otomatik build ve deploy
- Environment variable'lar Coolify UI'dan yonetilir (.env dosyasi gerekmez)
- Otomatik restart, health check, log yonetimi
- Dockerfile zaten hazir — sifir ek is

## Deployment Plani

### 1. VPS Gereksinimleri

| Kaynak | Minimum | Onerilen |
|--------|---------|----------|
| CPU | 1 vCPU | 2 vCPU |
| RAM | 2 GB | 4 GB |
| Disk | 20 GB SSD | 40 GB SSD |
| OS | Ubuntu 22.04/24.04 | Ubuntu 24.04 |
| Docker | 24+ | 27+ |
| Coolify | v4.x | v4.x |

### 2. Adimlar (Yarin)

#### Adim 1: GitHub Repo Hazirla

```bash
# Local'de
cd repo/
git remote add origin https://github.com/KULLANICI/hermes-agent.git
git push -u origin main
```

**.gitignore kontrol listesi:**
- `.env` —Coolify UI'dan environment variable olarak girilecek
- `venv/` — Docker build'da olusturulacak
- `__pycache__/` — Zaten .gitignore'da
- `temp_vision_images/` — Gecici dosyalar

#### Adim 2: Coolify'da Proje Olustur

1. Coolify dashboard → **Add New Resource** → **Application**
2. **Source**: GitHub repository sec (hermes-agent)
3. **Build Pack**: Dockerfile (otomatik algilanir)
4. **Branch**: main
5. **Port**: 8000 (web dashboard icin)
6. **Volume**: `/opt/data` — kalici veri deposu

#### Adim 3: Environment Variables (Coolify UI)

Coolify UI'da "Environment Variables" bolumune eklenecekler:

```
OPENROUTER_API_KEY=sk-or-v1-...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_ALLOWED_USERS=6030287709
TERMINAL_TIMEOUT=60
TERMINAL_LIFETIME_SECONDS=300
BROWSER_INACTIVITY_TIMEOUT=120
BROWSER_SESSION_TIMEOUT=300
```

#### Adim 4: Deploy

Coolify "Deploy" butonuna bas → otomatik:
1. GitHub'dan kod cek
2. Dockerfile ile build
3. Container baslat
4. Health check

#### Adim 5: Hermes-Wiki Entegrasyonu

Hermes-Wiki (cclank/Hermes-Wiki) repo'su 36 sayfalik kaynak-kodu dogrulanmis mimari dokumantasyon.
Bunu skill olarak Hermes'e baglayacagiz:

```bash
# VPS'te wiki'yi klonla
git clone https://github.com/cclank/Hermes-Wiki.git /opt/hermes-wiki

# config.yaml'a ekle (Coolify volume icinde /opt/data/config.yaml)
```

**config.yaml'a eklenecek:**
```yaml
skills:
  creation_nudge_interval: 15
  external_dirs:
    - /opt/hermes-wiki
```

Bu sayede Hermes:
- 36 konsept sayfasini skill olarak gorebilir
- Agent loop, memory sistemi, tool mimarisini bilir
- Kendi nasil calistigini anlar → "iki beyin" gerceklesir

#### Adim 6: Hermes Control Interface (HCI) Kurulumu

HCI — Hermes Agent icin web dashboard (v3.4.0). Ayri bir konteyner olarak calisir.

```bash
# VPS'te klonla
git clone https://github.com/xaspx/hermes-control-interface.git /opt/hci
cd /opt/hci

# Bagimliliklar
npm install
npm run build

# Yapilandir
cp .env.example .env
# .env icine:
#   HERMES_CONTROL_PASSWORD=<sifre>
#   HERMES_CONTROL_SECRET=$(openssl rand -hex 32)
#   HERMES_CONTROL_HOME=/opt/data
#   PORT=10272
```

Coolify'da ikinci uygulama olarak eklenebilir, veya systemd service olarak:
```bash
sudo systemctl enable hci
sudo systemctl start hci
# → http://VPS-IP:10272
```

**HCI Ne Saglar:**
- Web uzerinden ajan yonetimi (baslat/durdur/yeniden baslat)
- Gercek zamanli chat + tool call kartlari
- Token analizi + maliyet takibi
- Dosya gezgini + editor
- Skill pazari yonetimi
- Cron job yonetimi
- RBAC (28 izin, 3 rol)
- Terminal (browser uzerinden)

#### Adim 7: Dogrulama

- Telegram bot'una mesaj gonder → yanit vermeli
- Coolify logs → hata yok mu kontrol et
- Container status → running olmali
- `skill_view` ile wiki sayfasi okuyabildigini dogrula
- HCI → http://VPS-IP:10272 → dashboard acilmali

### 3. Coolify'da Docker Ayarlari

**Hermes Agent:**

| Ayar | Deger |
|------|-------|
| Dockerfile | `./Dockerfile` |
| Context | `.` |
| Port | 8000 |
| Volume | `/opt/data` |
| Restart Policy | unless-stopped |

**HCI (ayri uygulama):**

| Ayar | Deger |
|------|-------|
| Port | 10272 |
| Env | HERMES_CONTROL_PASSWORD, HERMES_CONTROL_SECRET |
| Volume | `/opt/data` (Hermes ile ayni volume) |

### 4. VPS Saglayici Tavsiyesi

- **Hetzner Cloud** — EUR 4-7/ay (CX22: 2vCPU, 4GB, 40GB) — en iyi fiyat/performans
- **Contabo** — EUR 5-7/ay (daha fazla RAM ama daha yavas disk)
- **DigitalOcean** — $6-12/ay (kolay arayuz)

## Yapilacaklar Listesi

- [ ] GitHub'da private repo olustur
- [ ] Repo'yu push et
- [ ] VPS al (Hetzner onerilen)
- [ ] Coolify erisimi dogrula
- [ ] Coolify'da uygulama olustur (Hermes Agent)
- [ ] Environment variable'lari gir
- [ ] Hermes-Wiki'yi VPS'e klonla (`git clone ... /opt/hermes-wiki`)
- [ ] config.yaml'a wiki path ekle
- [ ] Deploy et (Hermes Agent)
- [ ] HCI kurulumu (npm install + build + systemd)
- [ ] HCI .env yapilandir (sifre + secret)
- [ ] Telegram bot testi
- [ ] Wiki entegrasyonu dogrula (skill_view ile)
- [ ] HCI dashboard dogrula (http://VPS-IP:10272)

## Sources

- [Dockerfile](../repo/Dockerfile)
- [Docker entrypoint](../repo/docker/entrypoint.sh)
- [docker-compose.yml](../repo/docker-compose.yml)

## Related

- [[hermes-agent-kurulum]]
- [[002-telegram-entegrasyonu]]
- [[001-windows-wsl2-mi-yerel-mi]]
