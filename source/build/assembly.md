# Assembly tutorials

The assembly documentation is organized as one versioned guide per module. Each guide begins with its module-specific materials and uses the same item identifiers as the Master BOM.

```{admonition} Release status
:class: warning
The current module documents are marked `0.1-draft` and have not yet been assigned a hardware revision or verification date. Use them for the current team build, but complete the validation items in the project backlog before calling the documentation a public `1.0` release.
```

## Enclosure

| Module | Scope | Guide |
| --- | --- | --- |
| Frame and enclosure (`MOD-FRM`) | Base, pillars, walls, door, top panel, and module installation | {doc}`Open guide <assembly-tutorials/modules/mod-frm-assembly>` |

## Sub-modules

| Module | Scope | Guide |
| --- | --- | --- |
| Water bottle mount (`MOD-BMT`) | Bracket preparation and enclosure mounting | {doc}`Open guide <assembly-tutorials/modules/mod-bmt-assembly>` |
| Feeder (`MOD-FDR`) | Housing, motor, rotor, PCBs, and cabling | {doc}`Open guide <assembly-tutorials/modules/mod-fdr-aseembly>` |
| Light ring (`MOD-LGT`) | Housing, PCB, cap, and diffuser | {doc}`Open guide <assembly-tutorials/modules/mod-lgt>` |
| Photobeam gate (`MOD-PBG`) | Passage, IR boards, controller, cabling, and covers | {doc}`Open guide <assembly-tutorials/modules/mod-pbg-assembly>` |
| Screen (`MOD-SCR`) | Touchscreen, controller PCB, IR boards, cabling, and housing | {doc}`Open guide <assembly-tutorials/modules/mod-scr-assembly>` |

## Recommended workflow

1. Review the {doc}`safety` notes.
2. Download and check the {doc}`bom`.
3. Prepare the fabricated parts described in {doc}`fabrication`.
4. {doc}`Flash the required cards <../hardware/flashing-cards>` before installing them in any module.
5. Assemble the water bottle mount, feeder, light ring, photobeam gate, and two screen modules.
6. Assemble the frame and install the completed sub-modules.
7. Complete electrical, mechanical, and animal-facing safety checks before use.

## Reporting corrections

Report a tutorial or BOM discrepancy in the [assembly-tutorials issue tracker](https://github.com/Open-BeatBox/assembly-tutorials/issues). Include the item ID, module ID, hardware revision, tutorial section, and a photograph where useful.

```{toctree}
:hidden:
:maxdepth: 1

assembly-tutorials/tutorials_index
assembly-tutorials/conventions
assembly-tutorials/modules/mod-frm-assembly
assembly-tutorials/modules/mod-bmt-assembly
assembly-tutorials/modules/mod-fdr-aseembly
assembly-tutorials/modules/mod-lgt
assembly-tutorials/modules/mod-pbg-assembly
assembly-tutorials/modules/mod-scr-assembly
```
