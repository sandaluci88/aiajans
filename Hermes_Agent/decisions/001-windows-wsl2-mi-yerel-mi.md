---
title: Windows Kurulum Yaklasimi
tags: [decision, setup, windows, wsl2]
source: raw/sources/hermes-readme.md
date: 2026-04-21
status: active
brain: A
---

# Karar: Windows Kurulum Yaklasimi

## Baglam

Hermes Agent resmi olarak Windows native desteklemiyor. README'de "WSL2 kullanin" deniyor. Ancak:
- Python 3.11 Windows'da mevcut
- uv Windows'da mevcut
- pyproject.toml'da `pywinpty` destegi var

## Karar

**Windows native uzerinden denenecek, basarisiz olursa WSL2'ye gecilecek.**

### Gerekce

1. `uv` ve Python 3.11 Windows'da hazir
2. Git Bash mevcut, bash scriptler calisabilir
3. WSL2'ye gecis fallback olarak kullanilabilir
4. VPS deploy icin Linux olacak, yerel gelistirme icin Windows yeterli

### Riskler

- Bazibash scriptler Windows'da calismayabilir
- `pty` modulu sorunlari olabilir
- Docker entegrasyonu farkli calisabilir

## Sources

- [Hermes README](../raw/sources/hermes-readme.md)
- [Hermes pyproject.toml](../raw/sources/hermes-pyproject.toml)

## Related

- [[hermes-agent-genel-bakis]]
- [[hermes-kurulum-kararlari]]
