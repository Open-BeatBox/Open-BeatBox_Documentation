# Changelog

Notable changes to the Open-BEATBox manual. Keep entries concise and link to pull requests or issues when useful.

## Unreleased

- Zenodo DOIs of release `biorxiv-v1` added to the repositories page, the status page (D5) and `CITATION.cff` (Hardware 10.5281/zenodo.24080048, Software 10.5281/zenodo.24080479, Documentation 10.5281/zenodo.24080481).
- Repositories page: "Citing Open-BEATBox" section (preprint plus the Zenodo record of the release used; DOI placeholders until the `biorxiv-v1` drafts are published), version table aligned on release `biorxiv-v1`, note on the MATLAB/Arduino implementation and analysis code that are not yet public.
- Status page: D5 reworded (releases are drafts), D6 added (analysis code and dataset to be published before preprint v2).
- Protocols and video-tutorials pages: citation and Zenodo wording updated; landing page points to the citing section.

## biorxiv-v1 — 3 November 2026

- Release that accompanies the bioRxiv preprint; archived on Zenodo.
- The assembly tutorials and the Master BOM are now part of this repository (`source/build/assembly-tutorials/`, imported with history from the archived `assembly-tutorials` repository), so release archives are complete.
- CAN protocol page synced with the specification of 6 October 2026 (feeder section now matches the code); section 8 lists the remaining differences.
- Status page: firmware tests pass, the Firmware repository is a pointer, the PC-application refactor is not in the release.
- Flashing guide: archive downloads of the Software repository lack the two submodule libraries.
- Citation metadata (`CITATION.cff`, `.zenodo.json`) with the preprint author list.

## Earlier changes

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
