# Circuit boards (PCBs)

Open-BEATBox uses **eight circuit-board designs**, all drawn in [KiCad](https://www.kicad.org/) and stored in the `electronics/` folder of the [Hardware repository](https://github.com/Open-BeatBox/Open-BeatBox_Hardware/tree/main/electronics). Each design has its own folder with the same structure.

All boards are built around the **RP2040** microcontroller and talk over the **CAN bus** using the **MCP25625** controller, and share the same core circuit. Only the parts needed for a board's function are added.

## The eight boards

| Board (folder) | Quantity per box | Module | What it does |
| --- | ---: | --- | --- |
| `BB_RPI_shield_V1` | 1 | Main | Connection to the computer; distributes 5 V and 12 V; microSD slot; real-time clock; CAN communication with every module |
| `BB_feeder_main_V1` | 1 | Feeder | Controls pellet distribution with an **A4988** driver and a **14HM11-0404S** stepper motor |
| `BB_feeder_IRBarrier_V1` | 1 | Feeder | Infrared photo-interrupter **GP1A57HRJ00F** that detects pellets in the feeder |
| `BB_lighting_V1` | 1 | Lighting | Drives 5000 K white, 615 nm red and 940 nm infrared LEDs through a **PCA9955B** driver |
| `BB_screen_main_V1` | 2 | Screens | Drives a 2.8″ TFT screen with touch (ILI9341, Adafruit) over an 8-bit parallel bus; backlight control |
| `BB_IR_light_curtain_V2_38k` | 6 | Screens and tunnel | Pairs of boards that emit and detect **38 kHz** pulsed infrared beams (insensitive to room light); individual beam states (tunnel) and a combined output (screens) |
| `BB_tunnel_V1` | 1 | Tunnel | Reads a pair of light-curtain boards to find the direction and speed of movement; Qwiic connector; free pins for expansion |
| `BB_nosepoke_V1` | 1 | Nosepoke | Infrared photo-interrupter **GP1A57HRJ00F** for nose-poke detection |

The quantity of `BB_IR_light_curtain_V2_38k` is 6 because each of the two screens uses two (four in total) and the tunnel uses two.

## How the boards map to the assembly tutorials

The tutorials and the {doc}`Master BOM <../build/bom>` use their own item identifiers. This table connects them to the board folders in the Hardware repository.

| BOM item | Tutorial | Board folder |
| --- | --- | --- |
| `PCB-FDR-001` | Feeder (`MOD-FDR`) | `BB_feeder_main_V1` |
| `PCB-FDR-002` | Feeder (`MOD-FDR`) | `BB_feeder_IRBarrier_V1` |
| `PCB-LGT-001` | Light ring (`MOD-LGT`) | `BB_lighting_V1` |
| `PCB-PBG-001` | Photobeam gate (`MOD-PBG`) | `BB_tunnel_V1` |
| `PCB-PBG-002` (×2) | Photobeam gate (`MOD-PBG`) | `BB_IR_light_curtain_V2_38k` |
| `PCB-SCR-001` (×2) | Screen (`MOD-SCR`) | `BB_screen_main_V1` |
| `PCB-SCR-002` (×4) | Screen (`MOD-SCR`) | `BB_IR_light_curtain_V2_38k` |
| *(no BOM row yet)* | — | `BB_RPI_shield_V1` (main module) |
| *(no BOM row yet)* | — | `BB_nosepoke_V1` |

```{admonition} Known gap
:class: warning
The Master BOM does not yet contain rows for the main module board or the nosepoke board, and no tutorial builds the main module. Until it does, use the board folders above and the information on this page. See {doc}`../project/status`.
```

## What is inside each board folder

```text
BB_feeder_main_V1/
├── BB_feeder_main_V1.kicad_pro     KiCad project (open this one)
├── BB_feeder_main_V1.kicad_sch     circuit schematic (what is connected to what)
├── BB_feeder_main_V1.kicad_pcb     board layout (where parts and tracks are)
├── BB_feeder_main_V1.pdf           schematic as a PDF — readable without KiCad
├── *.kicad_sch                     sub-sheets: CAN_bus, Driver, MCU, Power, Sensor …
└── production/
    ├── BB_feeder_main_V1.zip       Gerber files — what the PCB factory needs  (Git LFS)
    ├── bom.csv                     list of components and their LCSC part numbers
    ├── positions.csv               pick-and-place: where each part goes
    ├── designators.csv             reference designators
    └── netlist.ipc                 electrical test netlist
```

Other helpful folders:

- `electronics/STEPs/` — 3D models of the boards (useful to check they fit in a housing);
- `electronics/pictures/` — renders of each board.

You **do not need KiCad** just to order boards: the `production/` folder is enough. You need it only to inspect or modify a design.

## Additional components to order

The assembled boards are only part of the electronics. You will also need (see the BOM for exact references and current links):

| Item | Reference used in the design |
| --- | --- |
| 12 V power adapter | MEAN WELL **GST60A12-P1J** |
| Connector for the screen | Molex PicoBlade **15134-0300** |
| Connector for the tunnel | Molex PicoBlade **15134-0606** |
| DB9 cables (between modules) | RS PRO **EX-011-0.5MTR-BLK** |
| 2 × TFT screen | Adafruit **1770** (2.8″ with touch) |
| Stepper motor | **14HM11-0404S** |
| Mini camera | colour mini-HD 700TVL 1/3″ CMOS, 3.6 mm lens (CCTV/FPV type) |
| USB-C cable | to connect the computer |

Some connectors may not be available from the assembly service and must be ordered separately and soldered by hand.

## Notes on names and revisions

Folder names carry the board revision (`V1`; `V2_38k` for the light curtain, a 38 kHz design). Older documents use slightly different names for some boards — for example `BB_Feeder_main_V1.1`, `BB_RPi_shield_V1.1`, `BP_Lighting_V1.1`. Treat the folders in the Hardware repository as the reference and check the revision before ordering.

## Next

- {doc}`ordering-pcbs` — upload the files and order.
- {doc}`flashing-cards` — put the firmware on the boards.
