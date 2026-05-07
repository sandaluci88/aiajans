---
title: Telegram Entegrasyonu
tags: [decision, telegram, messaging, gateway]
source: raw/sources/hermes-env-example
date: 2026-04-21
status: active
brain: A
---

# Karar: Telegram Entegrasyonu

## Baglam

Hermes Agent'in mesajlasma gateway'i Telegram, Discord, Slack, WhatsApp ve Signal destekler. Kullanici Telegram uzerinden iletisim kurmak istiyor.

## Karar

**Telegram gateway aktif edildi.**

### Konfigurasyon

- Bot Token: @BotFather'dan alindi
- Allowed Users: Kullanici ID'si ile sinirlandi (guvenlik)
- Mod: Long polling (VPS'de webhook'a gecis yapilabilir)

### Gateway Baslatma

```bash
hermes gateway setup   # ilk kurulum
hermes gateway start   # baslat
```

## Sources

- [Hermes .env.example](../raw/sources/hermes-env-example)

## Related

- [[hermes-agent-genel-bakis]]
- [[hermes-mesajlasma-gateway]]
