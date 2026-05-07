---
title: Hermes Control Interface Genel Bakis
tags: [hci, dashboard, web-ui, management, monitoring]
source: https://github.com/xaspx/hermes-control-interface
date: 2026-04-22
status: active
brain: A
---

# Hermes Control Interface (HCI) v3.4.0

Hermes Agent icin self-hosted web dashboard. Browser uzerinden ajan yonetimi,
terminal, dosya gezgini, oturum incelemesi, cron yonetimi ve sistem metrikleri.

## Teknoloji

- **Frontend**: Vanilla JS + Vite + xterm.js
- **Backend**: Node.js + Express + WebSocket
- **Gereksinim**: Node.js v18+, 512 MB RAM

## 8 Sayfa

| Sayfa | Ne Yapar |
|-------|----------|
| Home | CPU/RAM/Disk, gateway status, token kullanimi (7 gun) |
| Agents | Multi-profile yonetimi, baslat/durdur/yeniden baslat |
| Chat | Gercek zamanli streaming chat, tool call kartlari, oturum devami |
| Usage | Token analizi, model bazli maliyet, platform bazli kullanim |
| Skills | Skill pazari, kurulu skill'ler, guncelleme |
| Maintenance | Doctor, backup, update, kullanici yonetimi |
| Files | Dosya gezgini + editor (~/.hermes kapsaminda) |
| Logs | Gateway loglari, hata loglari |

## Onemli Ozellikler

### Chat (Gateway API)
- Gercek zamanli SSE streaming
- Tool call kartlari (JSON viewer ile)
- Oturum devami (sayfa yenilemede bile)
- Durdur butonu (stream iptal)
- Multi-profile destegi

### RBAC (Rol Tabanli Erisim)
- 28 izin, 12 grup
- 3 rol: admin (tam), viewer (sadece oku), custom
- bcrypt sifre hashleme
- CSRF koruma

### Token Analizi
- Zaman araligi filtreleme (gun / 7 gun / 30 gun / 90 gun)
- Model bazli kullanim + maliyet
- Platform bazli kullanim (CLI, Telegram, WhatsApp vb.)
- En cok kullanilan araclar

### Guvenlik
- Skor: 7.0/10
- CSRF 21 endpoint'te
- XSS koruma
- Rate limiting (giris: 5 basarisiz/15dk, terminal: 30 komut/dk)
- Path traversal onleme

## Kurulum

```bash
# Klonla
git clone https://github.com/xaspx/hermes-control-interface.git
cd hermes-control-interface

# Bagimliliklar
npm install

# Yapilandir
cp .env.example .env
# .env icinde:
#   HERMES_CONTROL_PASSWORD=sifre
#   HERMES_CONTROL_SECRET=$(openssl rand -hex 32)

# Build
npm run build

# Baslat
npm start
# → http://localhost:10272
```

### Systemd Service (Production)

```ini
[Unit]
Description=Hermes Control Interface
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/path/to/hermes-control-interface
ExecStart=/usr/bin/node server.js
Restart=always

[Install]
WantedBy=multi-user.target
```

## Environment Variables

| Degisken | Zorunlu | Aciklama |
|----------|---------|----------|
| HERMES_CONTROL_PASSWORD | Evet | Giris sifresi |
| HERMES_CONTROL_SECRET | Evet | CSRF + auth secret |
| PORT | Hayir | Port (varsayilan: 10272) |
| HERMES_CONTROL_HOME | Hayir | Hermes home (varsayilan: ~/.hermes) |

## VPS Deploy Plani

HCI ve Hermes Agent ayri konteynerler olarak calisacak:

```
Coolify
├── Hermes Agent konteyneri (Python, Dockerfile)
│   └── Telegram gateway + LLM
└── HCI konteyneri (Node.js)
    └── Port 10272 → web dashboard
```

## Sources

- [GitHub](https://github.com/xaspx/hermes-control-interface)

## Related

- [[hermes-agent-kurulum]]
- [[003-vps-deployment-stratejisi]]
- [[hermes-wiki-butunlesme]]
