---
title: Hermes ve Wiki Butunlesmesi
tags: [concept, wiki, hermes, soul, skill, memory, iki-beyin]
source: decisions/003-vps-deployment-stratejisi.md
date: 2026-04-22
status: active
brain: AB
---

# Kavram: Hermes ve Wiki Butunlesmesi

## Sorun

Wiki (lokal markdown dosyalari) ile Hermes Agent (VPS'te calisan konteyner) su anda kopuk.
Hermes wiki'nin bilgilerinden nasil yararlanacak?

## Cozum: 3 Katmanli Butunlesme

```
Wiki (Insan + Claude Code)
    │
    ├── SOUL.md → Hermes'in kisiligi (BRAIN B - Dusunen)
    ├── Skills → Teknik prosedurler (BRAIN A - Uygulayici)
    └── Memories → Anahtar bilgiler (her iki beyin)
```

### Katman 1: SOUL.md — Kisilik ve Felsefe

**Nedir?** Hermes'in sistem prompt'u. Her mesajda yuklenir.
**Ne gider?** Wiki'deki kararlar, kavramlar, kullanici tercihleri.

```markdown
# Ornek SOUL.md (wiki'den uretilecek)

Sen Hermes Agent'sin. Kullanici Turkce konusuyor.

## Davranis Kurallari
- Teknik sorulara dogrudan, kisaca cevap ver
- Hata yapinca acikca itiraf et
- Gereksiz tekror yapma

## Bilinen Kararlar
- Windows native uzerinden calisiliyor (WSL2 fallback)
- LLM saglayici: OpenRouter
- Telegram uzerinden ulasiliyor

## Kullanici Tercihleri
- Detayli aciklama degil, ozet tercih ediyor
- Turkce iletisim, teknik terimler Ingilizce
```

**Nasil guncellenir?** Wiki'deki kararlar degistikce SOUL.md yeniden uretilir.

### Katman 2: Skills — Teknitel Prosedurler

**Nedir?** Hermes'in ogrenilebilir becerileri. SKILL.md formatinda.
**Ne gider?** Wiki'deki entity sayfalari ve teknik bilgiler.

Ornek skill'ler (wiki'den uretilebilir):
- `turkish-legal-search` — hukuki arama proseduru
- `telegram-bot-management` — Telegram bot yonetimi
- `vps-deployment` — deployment adimlari

**Skill formati:**
```markdown
---
name: skill-adi
description: Kisa aciklama
version: 1.0.0
---

# Skill Basligi
## Workflow
1. Adim 1
2. Adim 2
...
```

### Katman 3: Memories — Kalici Bilgiler

**Nedir?** Hermes'in `memories/` klasoru. Sohbetler arasi kalici bilgiler.
**Ne gider?** Wiki entities'lerden ozet bilgiler.

```
~/.hermes/memories/
├── api-keys.md         → Hangi API'ler aktif
├── user-prefs.md       → Kullanici tercihleri
├── architecture.md     → Proje mimari ozeti
└── known-issues.md     → Bilinen sorunlar
```

## iki Beyin Mapping

| Wiki Beyin | Hermes Mekanizma | Icerik |
|------------|------------------|--------|
| BRAIN A (Uygulayici) | Skills + Memories | Kod, mimari, teknik prosedurler |
| BRAIN B (Dusunen) | SOUL.md | Kararlar, felsefe, strateji |
| BRAIN AB (Ortak) | Memories | Kaynak ozetleri, genel bilgiler |

## Uretim Akisi

```
Wiki sayfalari
    │
    ├── decisions/*.md ────→ SOUL.md uretimi
    ├── entities/*.md ────→ Memories dosyalari
    ├── concepts/*.md ────→ SOUL.md + Memories
    └── issues/*.md  ────→ Memories (known-issues)
```

## VPS'te Yapilandirma

```bash
# Docker volume icerisinde
/opt/data/
├── .env                → API anahtarlari
├── SOUL.md             → Wiki'den uretilen kisilik
├── config.yaml         → Model ayarlari
├── memories/           → Wiki'den uretilen bilgiler
│   ├── api-keys.md
│   ├── user-prefs.md
│   └── known-issues.md
└── skills/             → Ek skill'ler
```

## Otomasyon Senaryosu (Gelecek)

1. Wiki'de yeni karar alindi → Claude Code SOUL.md gunceller → VPS'e push
2. Yeni entity olustu → Memories dosyasi olustur → VPS'e push
3. Hermes VPS'te calisirken → memory aracini kullanir → wiki bilgilerini okur

## Sources

- [Docker entrypoint](../repo/docker/entrypoint.sh)
- [Skill format](../repo/skills/dogfood/SKILL.md)
- [SOUL.md](../repo/docker/SOUL.md)

## Related

- [[ajan-ogrenme-dongusu]]
- [[003-vps-deployment-stratejisi]]
- [[hermes-agent-kurulum]]
