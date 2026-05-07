---
title: Hermes Agent Genel Bakis
tags: [hermes, agent, llm, nous-research]
source: raw/sources/hermes-readme.md
date: 2026-04-21
status: active
brain: AB
---

# Hermes Agent Genel Bakis

Nous Research tarafindan gelistirilen, kendini gelistiren AI ajan sistemi. Deneyimlerinden skill olusturur, kullanim sirasinda gelistirir ve her yerde calisir.

## Temel Ozellikler

- **TUI (Terminal UI)**: Cok satirli duzenleme, slash-komut otomatik tamamlama, konusma gecmisi
- **Coklu Platform**: Telegram, Discord, Slack, WhatsApp, Signal, CLI — tek gateway surecinden
- **Kapali Ogrenme Dongusu**: Ajan tarafindan kurateli yapilan bellek, periyodik Reminder'lar, otonom skill olusturma
- **Zamanlanmis Otomasyonlar**: Dahili cron planlayici, herhangi bir platforma teslimat
- **Delege Et ve Paralelistir**: Izole alt-ajanlar, RPC ile tool cagri

## Mimari Bilesenler

| Bilesen | Aciklama |
|---------|----------|
| `agent/` | Temel ajan mantigi ve transport katmanlari |
| `gateway/` | Mesajlasma gateway (Telegram, Discord, vb.) |
| `hermes_cli/` | CLI arayuz |
| `skills/` | Yetenek sistemi (40+ skill) |
| `tools/` | Araclar (40+ tool) |
| `plugins/` | Eklenti sistemi (bellek, context engine) |
| `cron/` | Zamanlayici |
| `environments/` | Terminal ortam yoneticisi |

## LLM Saglayicilar

OpenRouter (200+ model), Nous Portal, NVIDIA NIM, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, Anthropic, Ollama, Arcee AI, OpenCode Zen/Go, Qwen OAuth, Xiaomi MiMo

## Kurulum

```bash
# hizli kurulum
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# gelistirici kurulumu
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent && ./setup-hermes.sh
```

## Sources

- [Hermes README](../raw/sources/hermes-readme.md)
- [Hermes pyproject.toml](../raw/sources/hermes-pyproject.toml)
- [Hermes .env.example](../raw/sources/hermes-env-example)

## Related

- [[hermes-mimari]]
- [[hermes-llm-saglayicilar]]
- [[hermes-kurulum-kararlari]]
