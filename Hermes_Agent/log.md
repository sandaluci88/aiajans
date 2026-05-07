# Wiki Log — Hermes Agent

> Append-only zaman damgalı olay kaydı. En yeni olay en üstte.

| Tarih | Olay | Detay |
|-------|------|-------|
| 2026-04-22 | hci-inceleme | xaspx/hermes-control-interface v3.4.0 incelendi — web dashboard: 8 sayfa, RBAC, chat, token analizi, terminal |
| 2026-04-22 | hci-deploy-plan | HCI ayri konteyner/systemd olarak VPS'e eklendi, deployment planina 7 adim olarak yazildi |
| 2026-04-22 | hermes-wiki-klonlandi | cclank/Hermes-Wiki klonlandi — 36 konsept + 2 entity + 3 changelog sayfasi (kaynak-kodu dogrulanmis) |
| 2026-04-22 | wiki-entegrasyon-karari | Hermes-Wiki config.yaml external_dirs ile skill olarak baglanacak → ajan kendi mimarisini bilecek |
| 2026-04-22 | hermes-test-basarili | AIAgent.run_conversation() testi gpt-4o-mini ile basarili: 32 arac yuklu, 3.30s yanit suresi, $0.002 maliyet |
| 2026-04-22 | wiki-update | entities/hermes-agent-kurulum.md test sonuclari eklendi |
| 2026-04-22 | wiki-concept | hermes-wiki-butunlesme — SOUL.md + Skills + Memories 3 katmanli butunlesme kavrami olusturuldu |
| 2026-04-22 | soul-md-uretildi | docker/SOUL.md wiki kararlarindan uretildi — kisilik, baglam, davranis kurallari |
| 2026-04-22 | deployment-coolify | VPS'te Coolify var — GitHub→Coolify konteyner deploy stratejisi belirlendi |
| 2026-04-22 | deployment-dosyalar | docker-compose.yml ve scripts/setup-vps.sh olusturuldu |
| 2026-04-22 | wiki-decision | 003-vps-deployment-stratejisi GitHub→Coolify yaklasimi guncellendi |
| 2026-04-22 | wiki-issue | 002-windows-cli-encoding Windows CLI encoding ve prompt_toolkit hatasi belgelendi |
| 2026-04-22 | windows-encoding | cli.py interaktif modda prompt_toolkit Win32 hatasi; PYTHONIOENCODING=utf-8 zorunlu |
| 2026-04-21 | hermes-kurulum-tamam | hermes-agent 0.10.0 editable modda kuruldu, tum bagimliliklar yuklendi (fire, openai, anthropic, rich, edge-tts, exa-py, fal-client, parallel-web, firecrawl-py) |
| 2026-04-21 | openrouter-aktif | OPENROUTER_API_KEY .env'e eklendi, baglanti testi basarili (gpt-4o-mini ile "Merhaba" alindi) |
| 2026-04-21 | wiki-update | CLAUDE.md kulllanici talimatlarina gore tamamen yeniden yazildi (birinci kural, log formati, cok dosyali guncelleme) |
| 2026-04-21 | wiki-decision | 002-telegram-entegrasyonu Telegram gateway aktif edildi |
| 2026-04-21 | wiki-issue | 001-windows-unix-only-testler fcntl ve pwd modulleri Windows'da yok |
| 2026-04-21 | wiki-ingest-hermes | Hermes Agent README, AGENTS.md, pyproject.toml, .env.example wiki'ye aktarildi |
| 2026-04-21 | wiki-ingest-autoresearch | Autoresearch README wiki'ye aktarildi |
| 2026-04-21 | wiki-concept | ajan-ogrenme-dongusu kavram sayfasi olusturuldu |
| 2026-04-21 | wiki-decision | 001-windows-wsl2-mi-yerel-mi karar sayfasi olusturuldu |
| 2026-04-21 | wiki-setup | Wiki yapisi kuruldu |
