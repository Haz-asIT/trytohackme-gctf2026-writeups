# GCTF 2026 Write-ups

CTF write-ups from **GCTF 2026** by **Team trytohackme**.

> **Spoiler warning:** This repository contains full solution paths and flags.

These write-ups focus on the shortest reproducible path from challenge artifact to flag: inspect the checker, recover the essential transform, and reproduce only the logic needed to invert it.

## Solved challenges

| Challenge | Technique | Write-up |
| --- | --- | --- |
| Prime Crawl | Custom VM / prime search / XOR stream | [Read](./prime-crawl/) |
| Comprehend Me | Python 3.10 bytecode / XOR | [Read](./comprehend-me/) |
| Desk Switch | Stripped ELF / byte transform | [Read](./desk-switch/) |
| State Walk | State machine / path recovery | [Read](./state-walk/) |
| Menu Feistel | Stripped ELF / 2-round Feistel | [Read](./menu-feistel/) |

## Notes

- Commands were reproduced on Linux/Pwnbox-style environments.
- Challenge binaries and original attachments are not redistributed here; only analysis, solver code, and screenshots are included.
- All flags are shown for write-up purposes.
