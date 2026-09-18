# Open-BEATBox Documentation

Documentation sources for Open-BEATBox, an open-source, modular platform for
24/7 home-cage behavioral testing, autonomous operant conditioning, and
longitudinal monitoring. This repository holds three things:

- `source/` — the Open-BEATBox technical manual, written in Markdown (MyST) and
  built with [Sphinx](https://www.sphinx-doc.org/) using the Furo theme.
- `notes/` — project documentation notes: architecture, user guide, hardware
  build, data and analysis, development, operations, contributing, FAQ,
  changelog, content style, and project requirements.
- `assets/` — documentation media: CAD renders, photographs of the electronics
  and assembled modules, logos, GIFs, and presentation slides.

`requirements.txt` at the repository root pins the Python packages needed to
build the manual.

## How this repository is used

The Open-BEATBox website consumes this repository as a git submodule mounted at
`docs/`. That is why `source/` and `requirements.txt` sit at the root here: from
the website's point of view they appear as `docs/source/` and
`docs/requirements.txt`. The website builds the manual from those paths and
publishes it at <https://open-beatbox.github.io/docs/manual/>.

- Project website: <https://open-beatbox.github.io/>
- Published manual: <https://open-beatbox.github.io/docs/manual/>

## Nested submodule

`source/build/assembly-tutorials/` is itself a git submodule, pointing at
[Open-BeatBox/assembly-tutorials](https://github.com/Open-BeatBox/assembly-tutorials).
It supplies the per-module assembly tutorials, the conventions document, and the
master bill of materials. The manual will not build without it, so clone with
submodules:

```bash
git clone --recurse-submodules https://github.com/Open-BeatBox/Open-BeatBox_Documentation.git
```

If the repository is already cloned without them:

```bash
git submodule update --init --recursive
```

## Building the manual locally

```bash
pip install -r requirements.txt
python -m sphinx -b html source <output>
```

Replace `<output>` with any directory for the generated HTML, then open
`<output>/index.html`. Add `-d <doctrees>` to keep the Sphinx doctree cache
outside the output directory.

## Licence

The documentation, notes, and media in this repository are licensed under the
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)
licence. The full text is in [`LICENSE`](LICENSE). Content pulled in through the
`assembly-tutorials` submodule is covered by that repository's own licence.
