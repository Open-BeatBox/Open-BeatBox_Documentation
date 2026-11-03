---
title: "Assemble photobeam gate"
module_id: "MOD-PBG"
hardware_revision: ""
document_version: "0.1-draft"
last_verified: "YYYY-MM-DD"
---

# Photobeam Gate Assembly Instructions

## Parts and tools

Complete reference in [module BOM](../BOM.csv).

| item_id | category | description | quantity |
|---|---|---|---:|
| `PRT-PBG-001` | 3D-printed part | photobeam passage | 1 |
| `PRT-PBG-002` | laser-cut part | passage back cover | 2 |
| `PCB-PBG-001` | circuit board | beam gate controller PCB | 1 |
| `PCB-PBG-002` | circuit board | IR beam-break array PCB | 2 |
| `TBC-CBL-PBG-001` | cable assembly | Molex PicoBlade, 6-position, receptacle-to-receptacle, 600 mm | 4 |
| `FST-INS-M3-BRASS` | fastening hardware | M3 brass threaded insert for plastics | 18 |
| `FST-M3X6` | fastening hardware | M3 × 6 mm button-head socket screw | 18 |

---
## 1. Prepare the photobeam gate

### 1.1 Prepare the housing

1. Inspect the `PRT-PBG-001` photobeam passage for printing defects or residual material.
2. Clean all insert holes, PCB mounting points, and cable passages.
3. Inspect both `PRT-PBG-002` back covers for damage or debris, and clear all mounting holes.
4. Identify the correct orientation of the passage and both covers.

### 1.2 Install the threaded inserts

1. Place `PRT-PBG-001` on a flat, solid surface.
2. Install the 18 `FST-INS-M3-BRASS` M3 threaded inserts in their designated locations. Refer to the assembly video for positioning.
3. Keep each insert straight and press it fully into its seat.

**Checkpoint:** All threaded inserts are straight and fully seated.

---

## 2. Install the electronics

1. Connect two `TBC-CBL-PBG-001` 6-position PicoBlade cables to the `PCB-PBG-001` beam gate controller. Push each connector fully into place while avoiding excessive force on the PCB-mounted Molex connectors.
2. Connect the free end of each `TBC-CBL-PBG-001` cable to one `PCB-PBG-002` IR beam-break array PCB.
3. Install the first `PCB-PBG-002` on one side of the `PRT-PBG-001` passage:
   - route the connected PCB and cable through the passage;
   - run the cable through the dedicated channel along the bottom of the printed part;
   - orient the PCB so the emitter or receiver faces correctly across the passage;
   - secure it with two `FST-M3X6` M3 × 6 mm screws.
4. Install the second `PCB-PBG-002` on the opposite side and secure it with two `FST-M3X6` M3 × 6 mm screws.
5. Arrange the cable running along the bottom of the passage inside the dedicated channel. Use tape if needed to keep it in place. Refer to the assembly video for routing.
6. Position the `PCB-PBG-001` controller on the upper outside surface of the gate, on either side, and secure it with the specified `FST-M3X6` M3 × 6 mm screws.
7. Check that all wires have enough slack, with no sharp bends or tension, and that the two external connectors remain accessible from the selected side of the gate.

**Checkpoint:** Both IR beam-break boards are secure and correctly aligned, the controller PCB is mounted, and all cables are routed without tension or interference.

---

## 3. Close the photobeam gate

### 3.1 Install the back covers

1. Position both `PRT-PBG-002` back covers on `PRT-PBG-001`.
2. Check that all cables remain inside their intended routing channels.
3. Align the cover mounting holes with the threaded inserts.
4. Secure both covers using `FST-M3X6` M3 × 6 mm screws.

> **Caution:** Do not use the screws to force the covers closed. If a cover does not sit flat, check the cable routing before tightening.

**Checkpoint:** Both covers sit flush and no cables are pinched between the housing parts.
