---
title: "Assemble screen module"
module_id: "MOD-SCR"
hardware_revision: ""
document_version: "0.1-draft"
last_verified: "YYYY-MM-DD"
---

# Screen Module Assembly Instructions

## Parts and tools

Complete reference in [module BOM](../BOM.csv).

| item_id | category | description | quantity |
|---|---|---|---:|
| `PRT-SCR-001` | 3D-printed part | display frame | 2 |
| `PRT-SCR-002` | 3D-printed part | display back cover | 2 |
| `PCB-SCR-001` | circuit board | main screen PCB | 2 |
| `PCB-SCR-002` | circuit board | IR circuit board | 4 |
| `CMP-SCR-TFT-2.8` | purchased component | TFT LCD with touchscreen breakout board | 2 |
| `CBL-PICO-3P-50MM` | cable assembly | Molex PicoBlade cable assembly, 3-circuit, double-ended, 50 mm length | 4 |
| `FST-INS-M3-BRASS` | fastening hardware | M3 brass threaded insert for plastics, tapered, flush install | 19 |
| `FST-M3X6` | fastening hardware | M3 screw for screen/PCB mounting and enclosure closure; length and head type to confirm | 15 |
| `TOL-FORC` | tool | precision stainless-steel tweezers, serrated tips, 150 mm length | 1 |

---

## 1. Housing preparation

### 1.1 Prepare the printed parts and electronics

1. Inspect `PRT-SCR-001` and `PRT-SCR-002` for printing defects or deformation.
2. Clean all holes, insert seats, cable passages, and internal openings.
3. Verify that no residual printing material obstructs the PCB, screen, or cable mounting areas. 
4. We bought, the  TFT Breakout `CMP-SCR-TFT-2.8` comes with a series of header pins. Before using the TFT Breakout, you will need to solder the headers. 
   **Note:** If you have never done this before be sure to check out the [Adafruit Guide To Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering)

### 1.2 Install the threaded inserts

1. Install all required `FST-INS-M3-BRASS` inserts in `PRT-SCR-001` and `PRT-SCR-002`, including the lateral inserts.
2. Start each insert straight in its hole.
3. Support the housing on a flat, solid surface while installing the inserts.
4. Seat each insert fully before continuing.

> **Caution:** Do not brace the printed housing against your hand or body while applying force to an insert.

> **Caution:** Install the lateral inserts now. Access becomes difficult once the electronics and touchscreen are mounted.

## 2. Electronics installation

### 2.1 Install the IR light-curtain boards

1. Position the two `PCB-SCR-002` IR light-curtain boards in their lateral mounting locations on the `PRT-SCR-001` display frame.
2. Secure each IR board with two `FST-M3X8` M3 × 8 mm screws.

**Checkpoint:** Both IR light-curtain boards are secure, correctly oriented, and their connectors remain accessible.

### 2.2 Connect and install the touchscreen

1. Orient the `CMP-SCR-TFT-2.8` TFT touchscreen correctly in the `PRT-SCR-001` display frame and secure it with four `TBC-M3-FASTENER` M3 screws.
2. Orient the `PCB-SCR-001` main screen PCB with the logo facing up.
3. Connect one `CBL-PICO-3P-50MM` 3-circuit PicoBlade cable between one lateral connector on the `PCB-SCR-001` main screen PCB and the corresponding `PCB-SCR-002` IR light-curtain board.
4. Use connectors on the same side of both boards and push the Molex connectors fully into place.
5. Repeat for the opposite side using the second `CBL-PICO-3P-50MM` cable.
6. Route both cables between the `CMP-SCR-TFT-2.8` touchscreen and the `PCB-SCR-001` main screen PCB, keeping them clear of screw holes and housing closing surfaces.
7. Insert the `PCB-SCR-001` main screen PCB into the display frame and align it with the touchscreen headers.
8. Press the PCB fully into place and check that both cables remain contained between the touchscreen and PCB.
9. Secure the `PCB-SCR-001` main screen PCB with three `FST-M3X8` M3 × 8 mm screws.

> **Caution:** Do not fasten the PCB if either cable is trapped outside the space between the touchscreen and PCB. The cables should provide enough slack for assembly without creating loops that can be pinched during closure.

## 3. Close the screen module

### 3.1 Install the housing cover

1. Position `PRT-SCR-002` over the assembled screen module.
2. Check that all cables remain inside their intended routing areas.
3. Bring the two housing parts together without forcing them.
4. Secure the cover using the specified fasteners `TBC-M3-FASTENER` 
5. Check the housing perimeter for gaps or trapped cables.

> **Caution:** If the housing does not close freely, do not tighten the screws to pull it closed. Reopen the module and correct the cable routing first.
**Checkpoint:** The housing closes fully without pinching cables or placing strain on connectors.
