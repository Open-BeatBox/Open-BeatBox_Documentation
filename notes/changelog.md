# Changelog

Notable changes to the Open-BEATBox manual. Keep entries concise and link to pull requests or issues when useful.

## Unreleased

- Rewrote the manual around the real system (RP2040 modules, CAN bus, MicroPython firmware, PC application) and for non-programmers: new *How it works*, *Getting started*, *Glossary* and *Troubleshooting* pages.
- **Hardware:** per-module descriptions, the eight circuit boards (with the mapping to the BOM), mechanical files (V2 and V3), how to order boards, flashing the module boards.
- **Software:** installing and using the PC application, training stages S1–S4, configuration reference, data files.
- **Firmware:** architecture, deployment, validation CLI; CAN protocol specification updated to the Software repository, with a list of differences from the code.
- **Project:** repositories and licences, status and open points, contributing guide.
- Recorded the developers' answers of 2 October 2026: firmware is the reference over the CAN spec, the two modified libraries will be flattened then forked, tests are being cleaned up.
- Recorded that `CircuitPython_PCA9955B` is now included in the Software repository (MicroPython port, `dev_mpy` f73fbfe), so the lighting module deploys on a fresh clone.
- Removed the outdated generic notes (they described a different, hypothetical system).

## Template

- **Date / Version** — short description of the change.
  - Highlights: bullets of key updates.
  - Links: PRs/issues (e.g., #123).
