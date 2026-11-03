# Contributing

Open-BEATBox is open-source by design, and contributions of every size are welcome — a corrected typo, a photo of your build, a bug report, a new stage. You do not need to be a programmer to help.

## Ways to contribute

| If you… | You can… |
| --- | --- |
| Built a box | Report what was unclear or wrong in the tutorials; share photos, parts that worked as substitutes, and build notes |
| Run experiments | Report bugs, suggest improvements to the stages, share protocols and validation results |
| Write documentation | Fix and extend this manual; add screenshots; translate |
| Design hardware | Improve the BOM, the CAD or the boards; document revisions |
| Write code | Fix issues, improve performance, add stages or modules |

Ideas and questions are welcome in [GitHub Discussions](https://github.com/Open-BeatBox/Open-BeatBox.github.io/discussions). The organisation's contributing guide and code of conduct are in the [`.github` repository](https://github.com/Open-BeatBox/.github).

## Which repository takes what

| Contribution about… | Repository |
| --- | --- |
| Assembly tutorials, the Master BOM | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation/tree/main/source/build/assembly-tutorials) |
| CAD, enclosure, circuit boards | [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware) |
| PC application, module firmware, CLI | [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software) |
| This manual and its media | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation) |
| The website | [Open-BeatBox.github.io](https://github.com/Open-BeatBox/Open-BeatBox.github.io) |

Contributions are licensed under the licence of the repository they go to ({doc}`project/repositories`).

## Open points where help is most useful

See {doc}`project/status` for the full list. Good starting points: testing the installation and flashing instructions on your machine, adding screenshots of the current interface, confirming the points marked *please confirm*, and fixing the BOM gaps.

## Improving this manual

The manual is written in Markdown (MyST) and built with [Sphinx](https://www.sphinx-doc.org/) and the Furo theme. The source is in the `source/` folder of the Documentation repository.

### Edit a page

On any page of the published manual, use the *Edit this page* link (pencil icon) to open the source on GitHub, edit it, and propose the change as a pull request.

### Build it on your computer

```bash
git clone https://github.com/Open-BeatBox/Open-BeatBox_Documentation.git
cd Open-BeatBox_Documentation
pip install -r requirements.txt
python -m sphinx -b html source _build/html
```

Open `_build/html/index.html` in a browser. The build should finish **without warnings**; check the output before opening a pull request.

### Publishing

The website repository includes the Documentation repository as a Git submodule at `docs/`. After a change is merged into the Documentation repository, a maintainer updates the submodule pointer in the website repository; the deployment workflow then rebuilds the manual together with the website and publishes both.

```bash
cd Open-BeatBox.github.io
git submodule update --remote --recursive docs
git diff --submodule
git add docs && git commit -m "Update documentation"
```

### Writing style

- **Write for a non-programmer first.** Explain a technical term the first time you use it, and add it to the {doc}`glossary` if it is new.
- Say what the reader should *do* and what they should *see*. Prefer short steps, numbered lists and tables.
- State the **hardware revision** (V3) and the **software version** when it matters.
- Use descriptive link text (*the flashing guide*), never "click here".
- Mark uncertain statements openly rather than guessing, and add them to {doc}`project/status`.
- One top-level heading per page; keep the heading levels in order.
- Give every image a short text description.
- File names in lower case with hyphens.

## Reporting a problem

Open an issue in the matching repository and include the hardware revision, the software commit, what you did, what you expected and what happened ({doc}`troubleshooting`).
