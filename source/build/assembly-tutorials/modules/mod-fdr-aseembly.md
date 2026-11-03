---
title: "Assemble feeder module"
module_id: "MOD-FDR"
hardware_revision: ""
document_version: "0.1-draft"
last_verified: "YYYY-MM-DD"
---

# Feeder Module Assembly Instructions

## Parts and tools

Complete reference in [module BOM](../BOM.csv).

| item_id | category | description | quantity |
|---|---|---|---:|
| `PRT-FDR-001` | 3D-printed part | feeder main base | 1 |
| `PRT-FDR-002` | 3D-printed part | feeder front part | 1 |
| `PRT-FDR-003` | 3D-printed part | feeder back cover | 1 |
| `PRT-FDR-004` | 3D-printed part | feeder rotor | 1 |
| `PCB-FDR-001` | circuit board | main feeder PCB | 1 |
| `PCB-FDR-002` | circuit board | feeder IR barrier PCB | 1 |
| `CMP-FDR-MOT` | purchased component | stepper motor | 1 |
| `CBL-PICO-3P-150MM` | cable assembly | 3-position PicoBlade cable assembly, 150 mm | 1 |
| `FST-M3X6-SHCS` | fastening hardware | M3 × 6 mm socket-head cap screw | 11 |
| `FST-M3X8-SHCS` | fastening hardware | M3 × 8 mm socket-head cap screw | 7 |
| `FST-INS-M3-BRASS` | fastening hardware | M3 brass threaded insert for plastics | 18 |
| `FST-NUT-M3-HEX` | fastening hardware | M3 hex nut | 18 |
| `TBC-TAPE` | adhesive / consumable | tape for temporary PicoBlade cable positioning | as required |

---

## 1. Prepare the feeder housing

### 1.1 Prepare the printed parts

1. Inspect `PRT-FDR-001`, `PRT-FDR-002`, `PRT-FDR-003`, and `PRT-FDR-004` for printing defects or residual material.
2. Clean all insert holes, PCB mounting points, cable passages, and the rotor area.
3. Verify that the cable tunnel in `PRT-FDR-001` is fully open.
4. Identify the correct orientation of the feeder base, front, back cover, and rotor.

### 1.2 Install the threaded inserts

1. Place the printed part on a flat, solid surface.
2. Install the required `FST-INS-M3-BRASS` threaded inserts in their designated locations on the feeder main base `PRT-FDR-001` (7 inserts) and on the feeder front part `PRT-FDR-002` (10 inserts)
3. Keep each insert straight and press it fully into its seat.
4. Repeat until all inserts required for the feeder assembly are installed.

## 2. Install the electronics

### 2.1 Install the IR barrier PCB

1. Position the `PCB-FDR-002` feeder IR barrier PCB on the feeder front part `PRT-FDR-002`.
2. Check that the IR sensor components are correctly oriented.
3. If a locating pin prevents the PCB from sitting flat, remove it carefully before mounting.
4. Secure `PCB-FDR-002` using the specified M3 hardware (`FST-M3X6-SHCS` x 2)

### 2.2 Route the IR barrier cable

1. Route the `CBL-PICO-3P-150MM` PicoBlade cable through the intended cable passage in `PRT-FDR-001`.
2. Position the cable as shown in the assembly reference.
3. Use `TBC-TAPE` if needed to hold the cable temporarily in place.
4. Leave both connectors accessible for later connection.

> **Caution:** Route and tape the cable on both ends before installing the main PCB `PCB-FDR-001` and the stepper motor `CMP-FDR-MOT` , as access becomes limited once the main PCB is mounted.

### 2.3 Install the stepper motor

1. Position the `CMP-FDR-MOT` stepper motor in `PRT-FDR-001`.
2. Orient the motor so its cables can reach `PCB-FDR-001` without tension and pass easily through the connecting hole.
3. Secure the motor using four `FST-M3X8-SHCS`  (M3 × 8 mm) screws.
4. Wire the motor to the PCB-FDR-001 main PCB before installing the board:
   1. Prep: Match each motor wire color to the color labels printed by the 4-terminal rising clamp. Twist bare wire ends tightly—ensure no stray strands remain.
   2. Open: Turn a terminal screw counterclockwise until the internal cage opens fully.
   3. Insert & Clamp: Slide the bare wire straight into the opening so the insulation sits flush at the entrance. Tighten clockwise until snug (do not over-tighten).
   4. Verify: Perform a light tug test. If the wire pulls free, ensure it sits inside the cage and re-clamp.
   5. Repeat for all four wires.

### 2.4  Install the main feeder PCB

1. Connect the `CBL-PICO-3P-150MM` PicoBlade cableto the `PCB-FDR-001`
2. Route all cables so they remain clear of the PCB mounting points and housing edges.
3. Position `PCB-FDR-001` in `PRT-FDR-001`.
4. Secure it with three `FST-M3X6-SHCS` M3 × 6 mm screws.

## 3. Install the back cover

1. Position `PRT-FDR-003` back cover on `PRT-FDR-001`.
2. Check that all cables remain inside their intended routing areas.
3. Secure the cover using four `FST-M3X6-SHCS` M3 × 6 mm screws.

## 4. Install the rotor

1. Install the required `FST-NUT-M3-HEX` M3 nut in the rotor assembly  `PRT-FDR-004`.
2. Insert one `FST-M3X8-SHCS` M3 × 8 mm screw through the intended access point.
3. Identify on the steppet motor shaft (or axle) the flat side (also known ar D-shaft). 
4. The rotor `PRT-FDR-004` goes onto the shaft. Align the side screw directly over the flat face of the motor shaft. Tighten the screw (though the access hole on the `PRT-FDR-001`) to force its tip flat against the motor shaft's flat surface, creating a mechanical lock.

## 5. Install the feeder front

1. Connect one end of the `CBL-PICO-3P-150MM` cable to `PCB-FDR-002`.
2. Push the PicoBlade connector fully into place and gently pull back to confirm it is seated.
3. Position `PRT-FDR-002` feeder front on `PRT-FDR-001`.
4. Confirm that the `PCB-FDR-002` IR barrier cable remains connected and clear of the mating surfaces.
5. Align the mounting holes.
6. Secure the feeder front with four `FST-M3X6-SHCS` M3 × 6 mm screws.

## 6. Final validation

### 6.1 Inspect the completed assembly

1. Confirm that the motor, rotor, both PCBs, and housing parts are secure.
2. Check that all connectors are fully seated.
3. Verify that the rotor area is free from dust and debris.
4. Inspect the animal-facing surface for gaps, sharp edges, or chew-accessible components.
5. Confirm that all cables are contained inside the housing and are not pinched.
