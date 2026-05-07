---
title: Windows CLI Encoding Hatasi
tags: [issue, windows, encoding, prompt_toolkit]
source: repo/cli.py
date: 2026-04-22
status: active
brain: A
---

# Sorun: Windows CLI Encoding Hatasi

## Belirti

`cli.py` calistirildiginda iki farkli encoding hatasi:

1. **cp1254 hatasi**: Windows terminal varsayilan kodlamasi cp1254 (Turkish), UTF-8 karakterler (banner ASCII art) encode edilemiyor
2. **prompt_toolkit Win32 hatasi**: Interaktif chat modunda `prompt_toolkit` Win32 console buffer erisimi saglayamiyor

```
UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-29
```
```
File "prompt_toolkit/output/win32.py", line 115, in __init__
    info = self.get_win32_screen_buffer_info()
```

## Kok Neden

1. Windows'un varsayilan terminal kodlamasi UTF-8 degil
2. Claude Code Bash ortami gercek bir Win32 console saglamiyor
3. `rich` kutuphanesi legacy Windows rendering moduna gecmeye calisiyor

## Cozum

### Kalici Cozum (Windows icin)

```powershell
# PowerShell'de UTF-8 zorla
$env:PYTHONIOENCODING = "utf-8"
python -X utf8 cli.py
```

veya Windows Settings → Time & Language → Administrative → Change system locale → Beta: Use Unicode UTF-8

### Gecici Cozum

```bash
# Tek seferlik
PYTHONIOENCODING=utf-8 python -X utf8 cli.py --query "soru"
```

### Claude Code Bash'te

`AIAgent.run_conversation()` dogrudan kullanilabilir (CLI yerine).
Interaktif mod gercek terminal (Windows Terminal, CMD) gerektirir.

## Etki

- Core agent (run_agent.py) duzgun calisiyor
- API baglantisi sorunsuz
- Sadece CLI'in interaktif modu etkileniyor
- VPS'te (Linux) bu sorun olmayacak

## Sources

- [cli.py](../repo/cli.py)
- [hermes_cli/banner.py](../repo/hermes_cli/banner.py)

## Related

- [[001-windows-wsl2-mi-yerel-mi]]
- [[hermes-agent-kurulum]]
