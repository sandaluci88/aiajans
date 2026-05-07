---
title: Windows pwd Modul Hatasi
tags: [issue, windows, test, unix-only]
source: tests/hermes_cli/test_gateway_service.py
date: 2026-04-21
status: active
brain: A
---

# Sorun: Windows pwd Modul Hatasi

## Belirti

`tests/hermes_cli/test_gateway_service.py` testinde `import pwd` hatasi aliniyor.

```
ModuleNotFoundError: No module named 'pwd'
```

## Kok Neden

`pwd` modulu Unix-only bir Python moduludur (POSIX parola veritabani erisimi). Windows'da mevcut degildir. Test dosyasi platform kontrolu yapmadan bu modulu import ediyor.

## Cozum

1. **Kisa vadeli**: Testi `--ignore` ile atla (mevcut yaklasim)
2. **Orta vadeli**: `sys.platform` kontrolu ekle veya `pytest.importorskip("pwd")` kullan
3. **Uzun vadeli**: Upstream'e PR gonder (platform-aware test)

## Etki

Gateway servisi disindaki tum testler Windows'da gecer. Gateway servisi Unix ortamlarinda zaten dogru calisir.

## Sources

- [Test dosyasi](../repo/tests/hermes_cli/test_gateway_service.py)

## Related

- [[001-windows-wsl2-mi-yerel-mi]]
