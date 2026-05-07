---
title: Ajan Ogrenme Dongusu
tags: [agent, learning-loop, skills, memory, self-improvement]
source: raw/sources/hermes-readme.md
date: 2026-04-21
status: active
brain: B
---

# Ajan Ogrenme Dongusu

Hermes Agent'in "closed learning loop" (kapali ogrenme dongusu) kavrami. Ajan deneyimlerinden ogrenir ve bu bilgiyi gelecek oturumlarda kullanir.

## Dongu Adimlari

```
Deneyim -> Skill Olusturma -> Kullanim Sirasinda Gelistirme -> Bellek -> Yeni Deneyim
```

## Bilesenleri

1. **Skill Olusturma**: Karmasik gorevlerden sonra otonom olarak skill olusturulur
2. **Skill Gelistirme**: Kullanim sirasinda skill'ler otomatik olarak iyilestirilir
3. **Periyodik Nudge'lar**: Ajanin bilgiyi kalici hale getirmesi icin hatirlatmalar
4. **Session Arama**: FTS5 tabanli oturum arama + LLM ozetleme
5. **Kullanici Modelleme**: Honcho ile capraz-oturum kullanici anlayisi

## Autoresearch ile Iliski

Autoresearch benzer bir donguyu model egitimi icin kullanir:
```
Kod Degisikligi -> 5dk Egitim -> Degerlendirme -> Tut/Geri Al -> Tekrarla
```

Bu iki dongu birlestirildiginde, ajan hem gorev bazli hem de model bazli ogrenme yapabilir.

## Sources

- [Hermes README](../raw/sources/hermes-readme.md)
- [Autoresearch README](../repo-autoresearch/README.md)

## Related

- [[hermes-agent-genel-bakis]]
- [[autoresearch-genel-bakis]]
- [[hermes-skill-sistemi]]
