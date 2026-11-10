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
| Open-BeatBox_Hardware | release `biorxiv-v1` | 2026-11-03 |
| Open-BeatBox_Software | release `biorxiv-v1` | 2026-11-03 |
| Open-BeatBox_Documentation (this manual, assembly tutorials and Master BOM) | release `biorxiv-v1` | 2026-11-03 |
| Open-BeatBox_Firmware | `main` (pointer to the Software repository; no code, no release) | 2026-11-03 |

When you build a box, record the version of each repository you used. The software and CAN protocol are still evolving ({doc}`status`).

## Citing Open-BEATBox

If you use Open-BEATBox in published work, please cite **both** the reference preprint and the archived release of the layer you used.

**The platform (preprint):**

> Euvrard M, Benzina N, Domingues D, Mondragón-González SL, Huzard D, Penderia G, Travert-Jouanneau Y, Lavielle O, Lousada E, Schreiweis C, Lorenz A, Pavlov P, Ajili Z, Lebegue L, Tissier P, Burguière E. "Open-BEATBox: an open-source autonomous operant chamber for high-throughput data acquisition of complex behaviour." bioRxiv, 2026. doi: [10.64898/2026.11.07.765109](https://doi.org/10.64898/2026.11.07.765109)

**The release you used (Zenodo record):**

| Layer | Repository | Release | Zenodo DOI |
| --- | --- | --- | --- |
| Hardware | [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware/releases) | `biorxiv-v1` | [10.5281/zenodo.24080048](https://doi.org/10.5281/zenodo.24080048) (all versions: [10.5281/zenodo.24080047](https://doi.org/10.5281/zenodo.24080047)) |
| Software (PC application and firmware) | [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software/releases) | `biorxiv-v1` | [10.5281/zenodo.24080479](https://doi.org/10.5281/zenodo.24080479) (all versions: [10.5281/zenodo.24080478](https://doi.org/10.5281/zenodo.24080478)) |
| Documentation (manual, tutorials, BOM) | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation/releases) | `biorxiv-v1` | [10.5281/zenodo.24080481](https://doi.org/10.5281/zenodo.24080481) (all versions: [10.5281/zenodo.24080480](https://doi.org/10.5281/zenodo.24080480)) |
| Firmware | [Open-BeatBox_Firmware](https://github.com/Open-BeatBox/Open-BeatBox_Firmware) | — | No record of its own: the firmware is in the Software repository, cite that record |

Each repository also has a `CITATION.cff` file, so GitHub's **Cite this repository** button gives you APA and BibTeX. Report the release tag (or commit) you built from, as asked in {doc}`../protocols/index`.

## Related repositories not yet public

The behavioural results in the preprint were obtained with the earlier MATLAB/Arduino implementation of the box, and analysed with MATLAB scripts. That implementation, the analysis code and the dataset are being prepared for publication (licence, authorship and a Zenodo DOI) and are not yet public; see {doc}`status` (D6).

## Where to report problems

| Problem with… | Issue tracker |
| --- | --- |
| Assembly tutorials or the BOM | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation/issues) |
| CAD, PCB or mechanical files | [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware/issues) |
| PC application or module firmware | [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software/issues) |
| This manual or the website | [Open-BeatBox.github.io](https://github.com/Open-BeatBox/Open-BeatBox.github.io/issues) |
| Questions, sharing builds | [Discussions](https://github.com/Open-BeatBox/Open-BeatBox.github.io/discussions) |
