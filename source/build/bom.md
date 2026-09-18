# Master bill of materials

The latest Master BOM is maintained alongside the modular assembly tutorials. It covers purchased components, custom parts, fasteners, tools, supplier references, fabrication files, quantities, and revision notes.

## Download

- {download}`BOM.xlsx — editable working file <assembly-tutorials/BOM.xlsx>`
- {download}`BOM.csv — portable version <assembly-tutorials/BOM.csv>`
- [Preview the CSV on GitHub](https://github.com/Open-BeatBox/assembly-tutorials/blob/main/BOM.csv)
- [Identifier conventions](https://github.com/Open-BeatBox/assembly-tutorials/blob/main/conventions.md)

The item IDs in the BOM, such as `PRT-FDR-001` and `PCB-SCR-002`, are the references used throughout the module tutorials. Proposed changes should preserve those IDs unless the physical item or compatibility contract changes.

```{admonition} Validation required before ordering
:class: warning
The current BOM still contains fields marked with questions, placeholder paths or suppliers, and duplicate identifiers. Pierre's technical review of the XLSX remains required before the BOM is tagged as a release. Do not treat unresolved rows as purchasing-ready.
```

## Required release checks

- Every required row has a quantity, specification, make/buy value, and supplier or fabrication source.
- Every custom part points to an existing, correctly cased CAD/PCB file.
- Each identifier is unique and matches every tutorial that uses it.
- Hardware and document revisions are stated.
- Required and optional items are clearly separated.
- The CSV and XLSX contain equivalent data.

Corrections belong in the [assembly-tutorials repository](https://github.com/Open-BeatBox/assembly-tutorials). The manual displays the pinned submodule revision and therefore remains traceable to the exact tutorial and BOM source used for the build.
