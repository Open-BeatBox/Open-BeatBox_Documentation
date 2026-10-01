# Fabrication

This page explains how to produce the physical parts: which files to use, how to make them, and what to check. The files themselves live in the [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware) repository; {doc}`../hardware/mechanical` describes how that repository is organised.

```{admonition} Download the big files correctly
:class: tip
`.STEP` and `.zip` files are stored with **Git LFS**. If you clone the repository, run `git lfs install` *before* cloning, or those files arrive as tiny text "pointer" files. Downloading a file from the GitHub web page always works.
```

## What to make

For the **V3** design (the one the tutorials build), each module folder under `mechanical/V3/` contains the module's CAD (`.STEP`), an archive of the native CAD project (`.zip`) and a `PRODUCTION/` folder with the print-ready files.

| What | Files | Process |
| --- | --- | --- |
| Feeder, lighting, main (Raspberry Pi shield) and screen housings | `mechanical/V3/<module>/PRODUCTION/*.STL` | 3D printing |
| Lighting module cover | `mechanical/V3/lighting/PRODUCTION/beatbox_lighting_cover.DXF` | Laser cutting |
| Enclosure panels: back walls (×2), feeder walls (×2), screen walls (×2), door walls (×2), door, door locker and ceiling in 3 mm; base plate in 10 mm | `mechanical/V3/enclosure/*.DXF` | Laser cutting (plexiglass) |
| Door knob | `mechanical/V3/enclosure/*.STL` | 3D printing |
| Corner pillars | `mechanical/V3/structure/*.STL` | 3D printing |
| Base plate | `mechanical/V3/structure/*.DXF` | Laser cutting |
| Complete assembly (for reference) | `mechanical/V3/final_assembly/*.zip` | — |

Part identifiers (`PRT-FDR-001` and so on) in the {doc}`Master BOM <bom>` refer to these files. Check that **every custom part in the BOM points to an existing file** before you start.

## 3D-printed parts

- The V2 production files were sliced for a Creality K1 Max with a 0.4 mm nozzle and a PLA filament, which is a reasonable starting point; use the profile you know works on your printer.
- Remove supports cleanly.
- Check for blocked insert seats and cable passages.
- Use tissue forceps to clear small imperfections.
- Avoid gouging mating surfaces.
- Do not drive M3 inserts above your hand — see {doc}`safety`.

## Plexiglass (laser-cut) parts

- Confirm wall colour decisions before production. Compare white, black and grey for tracking quality, reflections, contrast and illumination stability.
- Confirm the **matte side** orientation before assembly; it normally faces inward to reduce reflections.
- **Do not clean laser-cut plexiglass with alcohol**: it enters the laser-cut micro-cracks and causes cracking later.
- Wall thickness is 3 mm; the base plate is 10 mm.

## Circuit boards

Boards are not made at home: they are ordered from a PCB service using the Gerber, BOM and pick-and-place files in the Hardware repository. See {doc}`../hardware/ordering-pcbs` and {doc}`../hardware/pcbs`.

## Before assembly

- [ ] All parts are present and match the BOM.
- [ ] Insert seats and cable passages are clear.
- [ ] Panels are not cracked; matte side marked.
- [ ] Boards are received and visually inspected (no bridged solder, correct connectors).
- [ ] Boards are **flashed** ({doc}`../hardware/flashing-cards`).
