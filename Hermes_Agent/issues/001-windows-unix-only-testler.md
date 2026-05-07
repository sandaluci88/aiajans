---
title: Windows Unix-Only Testler
tags: [issue, windows, test, unix-only, fcntl, pwd]
source: tests/hermes_cli/test_gateway_service.py, tests/tools/test_file_sync_back.py
date: 2026-04-21
status: active
brain: A
---

# Sorun: Windows Unix-Only Testler

## Belirti

Windows'da iki test dosyasi Unix-only modul import ettigi icin basarisiz oluyor:

1. `tests/hermes_cli/test_gateway_service.py` → `import pwd`
2. `tests/tools/test_file_sync_back.py` → `import fcntl`

## Kok Neden

- `pwd` — POSIX parola veritabani erisimi (Unix-only)
- `fcntl` — POSIX dosya kilitleme (Unix-only)

Her iki modul de Python'in Unix-only yerlesik modulleridir. Windows'da mevcut degildir.

## Cozum

**Kisa vadeli** (mevcut): Bu testleri `--ignore` ile atla

**Orta vadeli**: `sys.platform` veya `pytest.importorskip()` ile platform kontrolu ekle

**Orta vadeli**: `conftest.py`'de skipif marker'i tanimla:
```python
import sys
import pytest

unix_only = pytest.mark.skipif(
    sys.platform == "win32",
    reason="Unix-only test"
)
```

## Etki

Bu dosyalarin test ettigi islevsellik (gateway servisi, dosya senkronizasyonu) Windows'da zaten desteklenmiyor. Testlerin atlanmasi Windows uyumlulugunu etkilemez.

## Sources

- [test_gateway_service.py](../repo/tests/hermes_cli/test_gateway_service.py)
- [test_file_sync_back.py](../repo/tests/tools/test_file_sync_back.py)

## Related

- [[001-windows-wsl2-mi-yerel-mi]]
