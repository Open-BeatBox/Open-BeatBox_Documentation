# Mechanical files

The `mechanical/` folder of the [Hardware repository](https://github.com/Open-BeatBox/Open-BeatBox_Hardware/tree/main/mechanical) holds the 3D models and production files for the enclosure and the modules, in **two generations**.

| Generation | Status | Format | Use it for |
| --- | --- | --- | --- |
| **V3** | **Current.** The design the assembly tutorials build. | Neutral formats (`.STEP`) plus native CAD archives (`.zip`) | Building a new box |
| **V2** | Previous generation, kept for reference | SolidWorks (`.SLDPRT`, `.SLDASM`) with renders | Understanding the history; adapting older designs |

## V3

```text
mechanical/V3/
├── enclosure/        laser-cut panels (.DXF, 3 mm) and the base plate (10 mm); door knob (.STL)
├── structure/        base plate (.DXF) and corner pillar (.STL)
├── feeder/           feeder.STEP, feeder.zip, PRODUCTION/ (.STL)
├── lighting/         lighting.STEP, lighting.zip, PRODUCTION/ (.STL + cover .DXF)
├── main/             main.STEP, main.zip, PRODUCTION/ (Raspberry Pi shield housing .STL)
├── screen/           screen.STEP, screen.zip, PRODUCTION/ (.STL)
├── tunnel/           tunnel.STEP, tunnel.zip, PRODUCTION/ (.STL)
└── final_assembly/   final_assembly.zip — the complete assembly
```

Each module folder follows the same pattern:

- **`<module>.STEP`** — the model in a neutral format that any CAD tool opens;
- **`<module>.zip`** — the native CAD project (for editing);
- **`PRODUCTION/`** — files ready to print or cut.

### Enclosure panels (laser cutting, 3 mm unless stated)

`back_wall_1`, `back_wall_2`, `ceiling`, `door`, `door_locker`, `door_wall_1`, `door_wall_2`, `feeder_wall_1`, `feeder_wall_2`, `screen_wall_1`, `screen_wall_2`, and `base_plate_10mm` (10 mm). The thickness is written in the file name.

## V2

SolidWorks sources, organised per module:

| Folder | Module |
| --- | --- |
| `baseCage/` | Base cage |
| `cage_1feeder_2screens/` | Cage assembly with one feeder and two screens (with a PDF drawing) |
| `camera/` | Camera and NeoPixel-ring support |
| `feeder/` | Feeder part and assembly |
| `passage/` | Passage |
| `screen/` | Screen frame |

Each has a `production/` subfolder with `.STL` meshes, `.DXF` outlines (the file name states the intended material and thickness, for example `..._3mm_clear.DXF`), and sliced `.gcode` whose names record the printer used (Creality K1 Max, 0.4 mm nozzle, Hyper PLA).

## File types in one minute

| Extension | What it is | Who needs it |
| --- | --- | --- |
| `.STL` | 3D mesh | Anyone 3D-printing: send it to your slicer |
| `.DXF` | 2D outline | Anyone laser-cutting: send it to the cutter |
| `.STEP` | Neutral 3D CAD | Anyone who wants to look at or modify the design |
| `.zip` (in module folders) | Native CAD project | Designers who want to edit the source |
| `.SLDPRT` / `.SLDASM` | SolidWorks (V2) | SolidWorks users only |

## Git LFS: do not skip this

`.zip` and `.STEP` files are stored with **Git LFS** because they are big. If you clone the repository without Git LFS you receive small text pointer files instead. Either install it first (`git lfs install`), or download the files from the GitHub web page.

## Known inconsistencies

- The Master BOM's `source_file_or_url` column still contains paths from the earlier repository layout (for example `02_CAD_files/V3/feeder_V3/PRODUCTION/feeder_base_V3.stl`). The matching file is now `mechanical/V3/feeder/PRODUCTION/feeder_base.STL`. See {doc}`../project/status`.
- `mechanical/README.md` in the Hardware repository is an unfilled changelog template.
