# Open-BEATBox User Manual

Open-BEATBox is an open-source, modular platform for 24/7 home-cage behavioral testing, autonomous operant conditioning, and longitudinal monitoring.

This manual is the main technical reference for building, understanding, and operating an Open-BEATBox. It brings the step-by-step assembly tutorials together with hardware, software, firmware, and experimental guidance in one place.

If you are assembling your first system, begin with **Build your own Open-BEATBox**. The build section takes you from preparation and the bill of materials through fabrication, module assembly, and final checks. Hardware and software reference pages are available when you need more detail about a component.

## Start here

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} Build your own Open-BEATBox
Follow the step-by-step workflow, from preparation and the bill of materials to module assembly and validation.

{doc}`build/index`
:::

:::{grid-item-card} Understand the hardware
Modules, PCB identifiers, feeder, screen, tunnel, lighting, and enclosure parts.

{doc}`hardware/index`
:::

:::{grid-item-card} Run experiments
Protocol templates, validation status, and experimental design notes.

{doc}`protocols/index`
:::

::::

```{toctree}
:maxdepth: 2
:caption: Documentation

overview
build/index
hardware/index
software/index
protocols/index
contributing
```

## Frequently used pages

- {doc}`Modular assembly tutorials <build/assembly-tutorials/tutorials_index>`
- [Master BOM (CSV and XLSX)](https://github.com/Open-BeatBox/assembly-tutorials#bill-of-materials)
- {doc}`Flashing the cards <hardware/flashing-cards>`
- [Open-source resources](https://github.com/Open-BeatBox)
- <a href="../../">Project website</a>
