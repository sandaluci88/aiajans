---
title: Hermes Agent Kurulum
tags: [hermes, kurulum, setup, openrouter]
source: raw/sources/hermes-readme.md
date: 2026-04-21
status: active
brain: A
---

# Hermes Agent Kurulum

## Genel Bilgi

Hermes Agent v0.10.0 — Nous Research tarafindan gelistirilen, kendini gelistiren AI ajan sistemi.

## Kurulum Durumu (2026-04-21)

| Bilesen | Durum | Not |
|---------|-------|-----|
| Repo klonu | OK | `repo/` klasorunde |
| venv | OK | Python 3.11.9 |
| hermes-agent paketi | OK | Editable modda kuruldu (`pip install -e .`) |
| fire | OK | v0.7.1 |
| openai | OK | v2.32.0 |
| anthropic | OK | v0.96.0 |
| rich | OK | v14.3.4 |
| edge-tts | OK | v7.2.8 |
| exa-py | OK | v2.12.0 |
| fal-client | OK | v0.13.2 |
| parallel-web | OK | v0.5.0 |
| firecrawl-py | OK | v4.22.3 |
| prompt_toolkit | OK | v3.0.52 |
| pydantic | OK | v2.12.5 |

## LLM Saglayici

- **Saglayici**: OpenRouter (`https://openrouter.ai/api/v1`)
- **API Anahtari**: `.env` dosyasinda `OPENROUTER_API_KEY` olarak tanimli
- **Baglanti Testi**: Basarili (gpt-4o-mini ile "Merhaba" response alindi)

## Entegrasyonlar

| Entegrasyon | Durum |
|-------------|-------|
| Telegram bot token | SET (`.env` icinde) |
| Telegram allowed users | SET |

## Test Sonuclari (2026-04-22)

| Test | Durum | Detay |
|------|-------|-------|
| OpenRouter API baglantisi | OK | gpt-4o-mini ile yanit alindi |
| Core agent import | OK | 32 arac yuklendi |
| AIAgent.run_conversation() | OK | 3.30s, 14,462 token, $0.002 |
| cli.py interaktif mod | HATA | prompt_toolkit Win32 console hatasi (yalnizca Claude Code Bash ortaminda) |
| cli.py --query modu | HATA | Ayni prompt_toolkit hatasi |

### Windows Encoding Notu

`cli.py` calistirilirken `PYTHONIOENCODING=utf-8` ve `python -X utf8` zorunlu.
Banner correct goruntuleniyor ama interaktif chat modu `prompt_toolkit` Win32 API erisimi
gerektiriyor. Gerçek terminalde (Windows Terminal, CMD) duzgun calismasi beklenir.

## Eksik / Yapilacak

- [ ] Varsayilan model secimi (`~/.hermes/config.yaml` ile `hermes model` komutu)
- [ ] `hermes setup` ile ilk kurulum sihirbazini calistirma
- [x] Ilk test calistirmasi (AIAgent.run_conversation ile basarili)
- [ ] Entity sayfalari cikarimi (raw/sources'tan kod bazli entity'ler)
- [ ] cli.py Windows terminal testi (gercek terminalde)
- [ ] VPS al ve deploy et (2026-04-23 plani)

## Deployment Dosyalari (Yeni)

| Dosya | Aciklama |
|-------|----------|
| `docker-compose.yml` | Docker Compose konfigurasyonu |
| `scripts/setup-vps.sh` | VPS tek komutla kurulum scripti |

## Komutlar

### Yerel (Windows)

```bash
# venv aktif et
cd repo && source venv/Scripts/activate

# Ajan calistir (API testi)
PYTHONIOENCODING=utf-8 python -X utf8 -c "from run_agent import AIAgent; ..."
```

### VPS (Ubuntu)

```bash
# Kurulum
bash scripts/setup-vps.sh

# Calistir
docker compose up -d --build

# Loglar
docker compose logs -f hermes

# Durdur
docker compose down
```

## Sources

- [Hermes README](../raw/sources/hermes-readme.md)
- [Hermes pyproject.toml](../raw/sources/hermes-pyproject.toml)

## Related

- [[hermes-agent-genel-bakis]]
- [[001-windows-wsl2-mi-yerel-mi]]
- [[003-vps-deployment-stratejisi]]
- [[002-windows-cli-encoding]]
- [[ajan-ogrenme-dongusu]]
