# Repositories and licences

Open-BEATBox is published as several repositories on GitHub, in the [Open-BeatBox](https://github.com/Open-BeatBox) organisation. Each "layer" of the project has its own repository and the open licence that suits it.

| Layer | Repository | Contents | Licence |
| --- | --- | --- | --- |
| **Hardware** | [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware) | CAD, enclosure, KiCad circuit boards, manufacturing files ({doc}`../hardware/index`) | CERN-OHL-S-2.0 |
| **Software** | [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software) | PC application, module firmware (MicroPython), validation CLI ({doc}`../software/index`) | AGPL-3.0 |
| **Firmware** | [Open-BeatBox_Firmware](https://github.com/Open-BeatBox/Open-BeatBox_Firmware) | Reserved for stand-alone firmware releases; no source published yet ({doc}`../software/firmware/index`) | GPL-3.0 |
| **Build guides** | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation/tree/main/source/build/assembly-tutorials) | Per-module assembly tutorials and the Master BOM ({doc}`../build/index`), kept with the manual | CC-BY-4.0 |
| **Documentation** | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation) | This manual and its media | CC-BY-4.0 |
| **Website** | [Open-BeatBox.github.io](https://github.com/Open-BeatBox/Open-BeatBox.github.io) | The public website and the pipeline that publishes the manual | AGPL-3.0 |

Each repository carries its own `LICENSE` file, which is authoritative for that layer, and a `CITATION.cff` file that GitHub uses for its **Cite this repository** button.

## How the pieces connect

```text
 Open-BeatBox.github.io  (website + build pipeline)
   └── docs/  ──────────────►  Open-BeatBox_Documentation  (this manual)
                                  └── source/build/assembly-tutorials/  (assembly tutorials, BOM)

 Open-BeatBox_Hardware ─┐
 Open-BeatBox_Software ─┼─ linked from the manual and the website (not built into them)
 Open-BeatBox_Firmware ─┘
```

- The **website** repository contains the website and a *Git submodule* `docs/` that points to the **Documentation** repository, which also holds the assembly tutorials and the Master BOM. Cloning the website with `--recurse-submodules` fetches both.
- Publishing builds the manual with Sphinx and the website with Next.js, and deploys both together to GitHub Pages. See {doc}`../contributing`.
- The **Hardware**, **Software** and **Firmware** repositories are independent: the manual links to them and describes them, but does not include their files.

## Which version does this manual describe?

This manual was last aligned with the following states of the repositories:

| Repository | Reference | Date |
| --- | --- | --- |
| Open-BeatBox_Hardware | `main` at `ecc81cd` | 2026-09-29 |
| Open-BeatBox_Software | `main` at `3877b26` | 2026-10-01 |
| Open-BeatBox_Firmware | `main` at `a221246` (licence, README and citation file only) | 2026-09-18 |
| assembly-tutorials | `03c4042` (documents marked `0.1-draft`) | 2026-09-15 |

When you build a box, record the version of each repository you used. The software and CAN protocol are still evolving ({doc}`status`).

## Where to report problems

| Problem with… | Issue tracker |
| --- | --- |
| Assembly tutorials or the BOM | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation/issues) |
| CAD, PCB or mechanical files | [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware/issues) |
| PC application or module firmware | [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software/issues) |
| This manual or the website | [Open-BeatBox.github.io](https://github.com/Open-BeatBox/Open-BeatBox.github.io/issues) |
| Questions, sharing builds | [Discussions](https://github.com/Open-BeatBox/Open-BeatBox.github.io/discussions) |
