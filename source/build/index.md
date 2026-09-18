# Build your own Open-BEATBox

This is the starting point for building an Open-BEATBox. The guide brings the preparation notes, bill of materials, fabrication guidance, and step-by-step module tutorials into a single workflow.

Before you begin, read the safety notes and check that the bill of materials matches the hardware revision you intend to build. Prepare and inspect the fabricated parts before assembling the modules. Cards must be flashed **before they are installed in a module**; see {doc}`Flashing the cards <../hardware/flashing-cards>` for the current status of those instructions.

```{toctree}
:maxdepth: 2
:hidden:

assembly
bom
safety
fabrication
video-tutorials
```

## Start the step-by-step guide

::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card} Module-by-module assembly
Follow the six Sphinx tutorials for the frame, bottle mount, feeder, light ring, photobeam gate, and screen. Each tutorial uses identifiers from the Master BOM and includes the available supporting media.

{doc}`Open the modular Sphinx guide <assembly-tutorials/tutorials_index>`
:::

::::

## Recommended build order

Complete every item in this preparation checklist before starting Step 1:

- Read the {doc}`safety notes <safety>` before handling tools, inserts, soldering equipment, or plexiglass.
- Download the Master BOM in {download}`XLSX <assembly-tutorials/BOM.xlsx>` or {download}`CSV <assembly-tutorials/BOM.csv>` format. Use the {doc}`BOM validation checklist <bom>` and {doc}`revision and identifier conventions <assembly-tutorials/conventions>` to resolve every incomplete field for the hardware revision being built.
- Prepare the 3D-printed and laser-cut parts using the {doc}`fabrication guide <fabrication>` and the [Open-BEATBox CAD and hardware files](https://github.com/Open-BeatBox/Open-BeatBox_Hardware).
- {doc}`Flash all required cards <../hardware/flashing-cards>` before installing them in their modules.

### Step 1 — Build the frame and enclosure

Follow the [frame and enclosure tutorial](assembly-tutorials/modules/mod-frm-assembly.md) to build the base, pillars, walls, and door. Stop before installing the additional modules or securing the top panel; return to that section in Step 7.

### Step 2 — Build the water bottle mount

Follow the [water bottle mount tutorial](assembly-tutorials/modules/mod-bmt-assembly.md) to build and prepare the mount for installation.

### Step 3 — Build the feeder module

Follow the [feeder module tutorial](assembly-tutorials/modules/mod-fdr-aseembly.md) to assemble the housing, electronics, motor, and rotor.

### Step 4 — Build the light ring module

Follow the [light ring tutorial](assembly-tutorials/modules/mod-lgt.md) to assemble the housing, PCB, cap, and diffuser.

### Step 5 — Build the photobeam gate

Follow the [photobeam gate tutorial](assembly-tutorials/modules/mod-pbg-assembly.md) to install the IR boards, controller, cables, and covers.

### Step 6 — Build the screen modules

Follow the [screen module tutorial](assembly-tutorials/modules/mod-scr-assembly.md) to build both touchscreen modules and install their controller PCBs, IR boards, and cabling.

### Step 7 — Integrate and validate the system

Return to the <a href="assembly-tutorials/modules/mod-frm-assembly.html#install-the-additional-modules">final section of the enclosure tutorial</a> to install the completed modules, position the photobeam gate, and secure the top panel. Complete the {doc}`safety notes <safety>` and every module checkpoint before use. Record deviations using the {doc}`module and item identifier conventions <assembly-tutorials/conventions>`, then report corrections through the [assembly-tutorials issue tracker](https://github.com/Open-BeatBox/assembly-tutorials/issues).

## Versioned sources

- {doc}`Step-by-step tutorial index <assembly-tutorials/tutorials_index>`
- {download}`Master BOM (XLSX) <assembly-tutorials/BOM.xlsx>`
- {download}`Master BOM (CSV) <assembly-tutorials/BOM.csv>`
- {doc}`Part-ID and media conventions <assembly-tutorials/conventions>`

The `assembly-tutorials` repository owns the editable module guides and BOM. It is included here as a pinned Git submodule, so the manual renders the reviewed source revision directly instead of maintaining a second editable copy.
