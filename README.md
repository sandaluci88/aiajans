# AI Ajans — Otomatik Pazarlama Ajansı Sistemi

Hermes + Paperclip + 58 Pazarlama Skill'i ile çalışan, çoklu müşteri destekli AI reklam ajansı.

## Mimari

```
Müşteri A (Telegram) ─┐
Müşteri B (Telegram) ──┤→ Paperclip (Org Layer, TR UI) ──→ Hermes (Execution)
Müşteri C (Telegram) ──┘     localhost:3100                  localhost:8642
```

| Katman | Araç | Görev |
|--------|------|-------|
| Orkestrasyon | Paperclip | Organizasyon, roller, bütçe, görev yönetimi |
| Execution | Hermes Agent | Skill çalıştırma, Telegram, cron, MCP |
| Araştırma | Autoresearch | Ajan geliştirme, otonom deneyler |

## Proje Yapısı

```
├── Hermes_Agent/           # Hermes Agent + Wiki
│   ├── repo/               # Hermes kaynak kodu (submodule)
│   ├── Hermes-Wiki/        # Wiki dokümantasyonu (submodule)
│   ├── sources/            # Kaynak özetleri
│   ├── concepts/           # Kavramlar
│   ├── decisions/          # Mimari kararlar
│   └── issues/             # Çözülen sorunlar
├── paperclip/              # Paperclip orkestrasyon (submodule, TR dil desteği)
├── paperclip-bridge/       # Hermes ↔ Paperclip köprüsü
│   ├── bridge.py           # API köprüsü
│   ├── config.yaml         # Müşteri organizasyon şablonu
│   ├── skill-role-map.yaml # 58 skill → 7 rol eşleştirmesi
│   └── Dockerfile          # Docker image
├── autoresearch/           # Karpathy autoresearch (submodule)
├── AI Ajans v1/            # Obsidian vault
└── docker-compose.coolify.yml  # VPS deploy
```

## 7 Ajan Rolü

| Rol | Skill Sayısı | Yetkinlik |
|-----|-------------|-----------|
| Pazarlama Direktörü (CMO) | 14 | Analitik, bütçe, strateji |
| SEO Uzmanı | 9 | AI-SEO, denetim, mimari |
| Medya Alıcısı | 17 | Google/Meta/LinkedIn/TikTok/Youtube Ads |
| İçerik Yazarı | 10 | Kopya, sosyal medya, e-posta |
| Görsel Üretici | 4 | Krea-AI, Pixa, Kie-AI |
| Video Üretici | 1 | Remotion |
| Büyüme Uzmanı | 14 | CRO, lead, churn, referans |

## Kurulum

### Gereksinimler

- Node.js 20+, pnpm 9.15+
- Python 3.11+
- Docker & Docker Compose (VPS)

### Local Geliştirme

```bash
# Submodule'leri yükle
git submodule update --init --recursive

# Paperclip
cd paperclip && pnpm install && pnpm dev

# Hermes
cd Hermes_Agent/repo && pip install -e ".[all]"

# Köprü
cd paperclip-bridge && pip install -r requirements.txt && python bridge.py
```

### VPS Deploy (Coolify)

```bash
# Environment variables
OPENROUTER_API_KEY=your_key
JWT_SECRET=your_secret
POSTGRES_PASSWORD=your_password

# Docker Compose ile başlat
docker compose -f docker-compose.coolify.yml up -d
```

Coolify'da:
1. Yeni proje oluştur
2. Git source: `https://github.com/sandaluci88/aiajans`
3. Compose dosyası: `docker-compose.coolify.yml`
4. Environment variables'ı gir
5. Deploy

## Yeni Müşteri Ekleme

`paperclip-bridge/config.yaml` dosyasına müşteri tanımı ekle:

```yaml
organizations:
  - name: "Müşteri Adı"
    prefix: "MUS"
    roles:
      - role: cmo
        label: "Pazarlama Direktörü"
        skills: [analytics-tracking, ads-budget]
```

## TR Dil Desteği

Paperclip arayüzü Türkçe'ye çevrilmiştir:

- `paperclip/ui/src/i18n/tr.ts` — 200+ Türkçe çeviri
- `paperclip/ui/src/i18n/context.ts` — `t()` fonksiyonu
- Sidebar, roller, durumlar, ayarlar Türkçe

## Submodule'ler

| Modül | Kaynak |
|-------|--------|
| Hermes Agent | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |
| Paperclip | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) |
| Autoresearch | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) |
| Hermes-Wiki | [cclank/Hermes-Wiki](https://github.com/cclank/Hermes-Wiki) |

## Lisans

Bu proje kendi kodları için MIT lisanslıdır. Submodule'ler kendi lisanslarına tabidir.
