---
title: Autoresearch Genel Bakis
tags: [autoresearch, karpathy, llm-training, self-improvement]
source: https://github.com/karpathy/autoresearch.git
date: 2026-04-21
status: active
brain: AB
---

# Autoresearch Genel Bakis

Karpathy'nin otonom arastirma ajan sistemi. Bir AI ajanina kucuk ama gercek bir LLM egitim ortami verir ve gece boyunca otonom deneyler yapmasina izin verir.

## Calisma Prensibi

1. Ajan `train.py` dosyasini duzenler
2. 5 dakikalik zaman butcesiyle egitir
3. Sonucu kontrol eder (val_bpb metrigi)
4. Iyilestirdi ise tutar, kotulesdi ise geri alir
5. Tekrarlar

## Onemli Dosyalar

| Dosya | Rol |
|-------|-----|
| `prepare.py` | Sabit sabitler, veri hazirlama (degistirilmez) |
| `train.py` | Model, optimizer, egitim dongusu (AJAN DEGISTIRIR) |
| `program.md` | Ajan talimatlari (INSAN DEGISTIRIR) |

## Gereksinimler

- NVIDIA GPU (H100 test edilmis)
- Python 3.10+
- uv paket yoneticisi
- PyTorch (CUDA 12.8)

## Hermes ile Entegrasyon

Hermes Agent'in "kendini gelistirme" mekanizmasi olarak kullanilabilir. Ajan, autoresearch uzerinden kendi egitim deneylerini yurutebilir.

## Sources

- [Autoresearch README](../repo-autoresearch/README.md)
- [Autoresearch program.md](../repo-autoresearch/program.md)

## Related

- [[hermes-agent-genel-bakis]]
- [[ajan-ogrenme-dongusu]]
