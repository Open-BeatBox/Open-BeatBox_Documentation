# Documentation and file conventions

An identifier answers “Which exact kind of item is this?” It must not depend on supplier, price, storage location, or assembly step.

## Pattern

Use `CATEGORY-MODULE-NUMBER` for custom items:

- `PRT-FDR-001` — custom feeder housing
- `PCB-FDR-001` — custom feeder PCB

Use `CATEGORY-SPECIFICATION` for interchangeable standard hardware shared by modules:

- `FST-M3X8-SHCS` — M3 × 8 mm socket-head cap screw
- `FST-NUT-M3-HEX` — M3 hex nut

## Categories

| Prefix | Category | Includes |
|---|---|---|
| `MOD` | Module | Feeder, screen, tunnel, light, frame |
| `PRT` | Custom mechanical part | 3D-printed, laser-cut, or machined pieces |
| `PCB` | Circuit board | Bare or assembled custom PCB |
| `CBL` | Cable assembly | A finished cable with defined length and terminations |
| `CON` | Connector item | Housing, crimp contact, header, socket, terminal |
| `FST` | Fastening hardware | Screws, nuts, washers, inserts, spacers, standoffs |
| `CMP` | Other purchased component | Motor, screen, sensor, hinge, power supply |
| `MAT` | Raw material | Plexiglass sheet, filament, bulk wire, tubing |
| `ADH` | Adhesive/chemical | Threadlocker, glue, solder, flux, grease |
| `TOL` | Tool | Hex key, crimp tool, soldering iron, multimeter |
| `MED` | Media | Photograph, video, diagram |
| `TST` | Test | Defined procedure with a pass criterion |

## Screws, nuts, washers, and inserts

All belong to `FST` because they are fastening hardware. Examples: 

| ID | Meaning |
|---|---|
| `FST-NUT-M3-HEX` | M3 standard hex nut |
| `FST-WSH-M3-FLAT` | M3 flat washer |

## Revisions and document versions

- Hardware revisions identify physical compatibility: `A`, `B`, `C`.
- Document versions identify editorial releases: `1.0`, `1.1`, `2.0`.
- Every page states the applicable module/hardware revision.

## Media filenames

Use: `<module-id>_<step>_<action>_<view>.<ext>`

Examples:

- `mod-fdr_03_install-motor_top.jpg`
- `mod-fdr_04_route-cable_close.jpg`
- `mod-fdr_05_check-rotor-motion_demo.mp4`
