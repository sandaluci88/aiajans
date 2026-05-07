# Wiki CLAUDE.md — Hermes Agent Vault

## Birinci Kural (TAŞA KAZINMIŞ)

**Her soruya cevap vermeden once** → `index.md`'yi ac, ilgili tum sayfalari baglama cek.
**Cevaptan sonra** → vault'u izin beklemeden guncelle, `log.md`'ye kayit dustur.
"Vault'u guncelleyeyim mi?" diye sormak YASAK — dogrudan yap.

Yalnizca geri donusu olmayan mudahalelerden once danis:
- Sayfa birlestirme
- Sayfa silme (archive'a tasima disinda)
- Buyuk capli tasimalar

## Amac

Bu klasor paylasilmis bir ikinci beyindir — hem insan hem LLM icin. LLM ile birlikte insa edilen, artimli, bakimli bir wiki'dir.

**Kaynak**: konusmalar, birakilan dosyalar (makale, PDF, gorsel, not), yapistirilan baglantilar, laf arasinda gecen fikirler, tepkiler, tercihler, kararlar, tekrar eden oruntuler. Hangi formatta veya ne kadar gelisiguzel gelirse gelsin, her girdi bir INGEST'tir.

## Dil

TUM wiki sayfalari Turkce yazilir. Teknik terimler (API, MCP, token, webhook vb.) Ingilizce kalabilir.

## Dosya Adlandirma

- kebab-case: `my-page-name.md`
- Bosuk, buyuk harf, ozel karakter yok

## Sayfa Formati

Her sayfa su yapiya uyar:

```markdown
---
title: Sayfa Basligi
tags: [etiket1, etiket2]
source: raw/kaynak-dosya.md
date: 2026-04-21
status: active | draft | archived
brain: A | B | AB
---

# Sayfa Basligi

Icerik buraya...

## Sources

- [Kaynak 1](../raw/sources/kaynak-1.md)

## Related

- [[ilgili-sayfa]]
- [[ilgili-kavram]]
```

## Klasor Yapisi

```
Hermes_Agent/
├── raw/sources/     → Ham kaynaklar, DOKUNULMAZ
├── raw/docs/        → Statik dokumanlar
├── raw/assets/      → Resimler, PDF'ler
├── sources/         → Her ham kaynak icin ozet sayfasi
├── entities/        → Dosyalar, fonksiyonlar, servisler, kisiler
├── concepts/        → Soyut kavramlar
├── decisions/       → Atomik kararlar (her karar = tek sayfa)
├── issues/          → Duzeltilen sorunlar (kok neden + fix)
├── syntheses/       → Ust duzey genel bakis sayfalari
├── archive/         → Eskimis sayfalar, asla silinmez
├── index.md         → Kategori bazli icerik katalogu
├── log.md           → Append-only zaman damgali olay kaydi
└── CLAUDE.md        → Bu dosya (wiki isletim el kitabi)
```

Yapi tamamen akiskandir — bilgi gerektirdikce sayfa ve klasorleri ac, bol, birlestir, yeniden duzenle. Bos iskelet kurma — klasor ve sayfa ancak icerik onu hak ettiginde dogar.

## Iki Beyin (BRAIN A / BRAIN B)

Bu wiki iki ayri beyni (perspektifi) barindirir. Her sayfa bir beyne aittir:

### BRAIN A — Uygulayici (Implementer)
- Odak: Nasil yapilir? Kod, mimari, teknik detay
- Soru kalibi: "Bu nasil calisir?" "Kodu nerede?" "Nasil kurulur?"
- Sayfa isareti: `brain: A` (frontmatter'da)
- Tipik icerik: entity sayfalari, kararlar, sorunlar

### BRAIN B — Dusunen (Thinker)
- Odak: Neden? Ne anlama gelir? Kavramsal derinlik, strateji
- Soru kalibi: "Bu ne demek?" "Neden boyle?" "Nereye gidiyor?"
- Sayfa isareti: `brain: B` (frontmatter'da)
- Tipik icerik: kavramlar, sentezler, stratejik kararlar

Ortak sayfalar (kaynak ozetleri, index) her iki beyne de aittir (`brain: AB`).

## Uc Operasyon Workflow'u

### INGEST (wiki-ingest)

1. `raw/` icindeki dosyalari oku
2. `sources/` altinda ozet sayfasi yaz
3. Ilgili `entity/`, `concept/`, `decision/` sayfalarini olustur veya capraz-guncelle
4. `index.md` katalogunu guncelle
5. `log.md`'ye olay kaydi ekle

Iligli wiki sayfalarini **izin beklemeden kendiliginden guncelle**.

### QUERY (wiki-query)

1. `index.md`'den ilgili sayfalari bul
2. Icerikleri oku ve sentezle
3. Her iddiaya kaynak referansi ver
4. Iyi cevaplari `syntheses/` veya `concepts/` altinda geri dosyala
5. `log.md`'ye sorgu kaydi ekle

### LINT (wiki-lint)

Yaklasik her 10 oturumda bir lint turu at. Tara ve raporla:
- Celiskiler (farkli sayfalarda tutarsiz bilgiler)
- Eskimis iddialar (tarihi gecmis veya gecersiz)
- Yetim sayfalar (hicbir yerden referans verilmeyen)
- Eksik kavram sayfalari (bahsedilen ama olusturulmamis)
- Tek yonlu cross-reference'lar (A→B var, B→A yok)
- Kaynak bosluklari (idsi kaynaksiz olanlar)
- Sormam gereken sonraki sorular
- `log.md`'ye lint raporu ekle

## Log Formatı

```markdown
## [YYYY-AA-GG] ingest|query|lint | baslik

- ne yapildi
- hangi sayfalar degisti
```

## Cok Dosyali Guncelleme Kurali

Her guncelleme cok dosyalidir:
1. Ilgili sayfalar
2. `index.md`
3. `log.md`

Asla tek noktaya boca etme. Capraz-referanslari iki yonlu yap.

## Hard Rules

1. **raw/ ASLA degistirilmez** — ham kaynaklar dokunulmazdir
2. **Kaynaksiz iddia yasak** — her iddia bir `raw/` dosyasina veya URL'ye referans vermelidir
3. **Sayfa silme yok** — eskimis sayfalar `archive/` klasorune tasınır, asla silinmez
4. **Celiskiler isaretlenir** — `## CELISKI` basligiyla acikca belirtilir, gizlenmez. Ikisini de tut, tarihlerini dus.
5. **Append-only log** — `log.md`'den hicbir satir silinmez
6. **Her karar atomik** — `decisions/` klasorunde her karar tek bir sayfadir
7. **Iki beyin etiketi zorunlu** — entity/concept/decision/synthesis sayfalarinda `brain: A|B|AB` frontmatter alani zorunludur
8. **Iyi sorgulara verilen cevaplar wiki sayfasina geri yazilir** — kesifler birike birike buyusun
9. **Her anlasmali alisveristen sonra vault guncellenir** — oturum kapanmadan once

## Bu Dosya Hakkında

Bu dosya tasa kazinmis degil, yasayan bir belgedir. Neyin isledigini gordukce uzerine yaz.
