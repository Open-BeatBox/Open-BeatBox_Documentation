# Open-BEATBox Documentation

This repository holds the documentation of **Open-BEATBox** (*Open — BEhavioural and AuTonomous operant Box*): an open-source, modular, low-cost platform for autonomous home-cage operant conditioning and long-duration behavioural data acquisition in rodents.

**Read the manual online: <https://open-beatbox.github.io/docs/manual/>**

The manual is written for people who build and use the box, not only for programmers. It explains how a trial flows from the animal to the data file, how to build the hardware, how to flash the boards, how to run experiments, and how the firmware and the CAN protocol work.

## Where to start

| I want to… | Start here |
| --- | --- |
| Understand what the box is and how it works | [Overview](https://open-beatbox.github.io/docs/manual/overview.html) and [How it works](https://open-beatbox.github.io/docs/manual/how-it-works.html) |
| Go from nothing to a first experiment | [Getting started](https://open-beatbox.github.io/docs/manual/getting-started.html) |
| Build one | [Build your own](https://open-beatbox.github.io/docs/manual/build/index.html) |
| Run experiments | [Software](https://open-beatbox.github.io/docs/manual/software/index.html) |
| Look up a word | [Glossary](https://open-beatbox.github.io/docs/manual/glossary.html) |
| Fix a problem | [Troubleshooting](https://open-beatbox.github.io/docs/manual/troubleshooting.html) |

## The Open-BEATBox repositories

| Layer | Repository | Licence |
| --- | --- | --- |
| Hardware (CAD, circuit boards) | [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware) | CERN-OHL-S-2.0 |
| Software (PC application, module firmware, CLI) | [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software) | AGPL-3.0-or-later |
| Firmware (placeholder; the firmware is in the Software repository) | [Open-BeatBox_Firmware](https://github.com/Open-BeatBox/Open-BeatBox_Firmware) | GPL-3.0 |
| **Documentation (this repository)**, including the assembly tutorials and Master BOM | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation) | CC-BY-4.0 |
| Website | [Open-BeatBox.github.io](https://github.com/Open-BeatBox/Open-BeatBox.github.io) | AGPL-3.0 |

## What is in this repository

```text
Open-BeatBox_Documentation/
├── source/             the manual: Markdown (MyST) built with Sphinx and the Furo theme
│   ├── index.md        landing page and navigation
│   ├── overview.md, how-it-works.md, getting-started.md, glossary.md, troubleshooting.md
│   ├── build/          build guide: BOM, fabrication, safety, assembly, first power-up
│   │   └── assembly-tutorials/   module assembly tutorials, conventions and the Master BOM
│   ├── hardware/       modules, circuit boards, mechanical files, ordering, flashing
│   ├── software/       PC application, stages, configuration, data, firmware, CAN protocol
│   ├── protocols/      behavioural protocols
│   ├── project/        repositories, status and open points
│   └── _static/        logo, stylesheet, small images used by the manual
├── notes/              maintainers' notes: changelog, content style, contributing, project-requirements template
├── assets/             full-size media: CAD renders, photographs, logos, slides
├── requirements.txt    Python packages needed to build the manual
└── LICENSE
```

## How this repository is used

The Open-BEATBox website consumes this repository as a Git submodule mounted at `docs/`. That is why `source/` and `requirements.txt` sit at the root here: from the website's point of view they appear as `docs/source/` and `docs/requirements.txt`. The website builds the manual from those paths and publishes it at <https://open-beatbox.github.io/docs/manual/>.

After a change is merged here, a maintainer updates the submodule pointer in the website repository so that the new version is published.

### Assembly tutorials

`source/build/assembly-tutorials/` holds the per-module assembly tutorials, the conventions document and the Master BOM. It used to be a separate repository ([Open-BeatBox/assembly-tutorials](https://github.com/Open-BeatBox/assembly-tutorials), now archived) included as a submodule; it was imported here with its history so that release archives are complete. Edit the tutorials and the BOM here.

## Building the manual on your computer

You need Python 3.10 or newer.

```bash
pip install -r requirements.txt
python -m sphinx -b html source _build/html
```

Then open `_build/html/index.html` in a browser. Add `-d <doctrees>` to keep the Sphinx cache outside the output folder. The build should end with *build succeeded* and **no warnings**.

## Citing

If you use this documentation, please cite it with the metadata in [`CITATION.cff`](CITATION.cff) (GitHub's *Cite this repository* button). Each release is archived on Zenodo with its own DOI.

## Contributing

Contributions are welcome — a typo fix, a screenshot, a correction after building your own box. See the [contributing guide](https://open-beatbox.github.io/docs/manual/contributing.html) in the manual, and the list of [open points](https://open-beatbox.github.io/docs/manual/project/status.html) where help is most useful.

## Licence

The documentation, notes and media in this repository are licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) licence. The full text is in [`LICENSE`](LICENSE).
