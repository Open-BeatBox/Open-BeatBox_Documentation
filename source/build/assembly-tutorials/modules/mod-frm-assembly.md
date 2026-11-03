---
title: "Assemble frame structure"
module_id: "MOD-FRM"
hardware_revision: ""
document_version: "0.1-draft"
last_verified: "YYYY-MM-DD"
---

# Assemble frame structure

## Parts and tools

Complete reference in [module BOM](../BOM.csv).

| item_id | category | description | quantity |
|---|---|---|---:|
| `TOL-HEXKEY-4MM` | tool | 4 mm hex key | 1 |
| `CMP-ENC-FOOT` | purchased component | adhesive rubber/polyurethane feet | 8 |
| `CMP-ENC-BIN` | purchased component | removable plastic enclosure bin | 1 |
| `PRT-ENC-001` | laser-cut part | enclosure base plate | 1 |
| `PRT-ENC-002` | 3D-printed part | enclosure support pillar | 4 |
| `PRT-ENC-003` | laser-cut part | feeder wall panel, first layer | 1 |
| `PRT-ENC-004` | laser-cut part | feeder wall panel, second layer | 1 |
| `PRT-ENC-005` | laser-cut part | screen wall panel, first layer | 1 |
| `PRT-ENC-006` | laser-cut part | screen wall panel, second layer | 1 |
| `PRT-ENC-007` | laser-cut part | master-module wall panel, first layer | 1 |
| `PRT-ENC-008` | laser-cut part | master-module wall panel, second layer | 1 |
| `PRT-ENC-009` | laser-cut part | door wall panel, first layer | 1 |
| `PRT-ENC-010` | laser-cut part | door wall panel, second layer | 1 |
| `PRT-ENC-011` | laser-cut part | enclosure door panel | 1 |
| `PRT-ENC-012` | laser-cut part | door locking element | 1 |
| `PRT-ENC-013` | 3D-printed part | enclosure door button | 1 |
| `PRT-ENC-014` | laser-cut part | clear enclosure top panel | 1 |
| `FST-INS-M3-BRASS` | fastening hardware | M3 brass threaded insert for plastics | 1 |
| `FST-NUT-M5-HEX` | fastening hardware | M5 hex nut | 8 |
| `FST-M5X50` | fastening hardware | M5 × 50 mm socket-head cap screw | 12 |
| `FST-M3X8` | fastening hardware | M3 × 8 mm hex-socket button screw | 16 |
| `FST-M3X10` | fastening hardware | M3 × 10 mm fastener | 2 |
| `FST-NUT-M3-HEX` | fastening hardware | M3 hex nut | 12 |
| `FST-HIN` | fastening hardware | door hinge | 2 |

---

# Enclosure Assembly Instructions

## 1. Base and pillar assembly

### 1.1 Prepare the base plate and pillars

1. Place the enclosure base plate `PRT-ENC-001` flat on a clean, level work surface.
2. Verify that all internal cutouts in `PRT-ENC-001` have dropped clear of the plate.
3. Verify that the internal holes of all four `PRT-ENC-002` support pillars are fully clear. If blocked, use a flathead screwdriver to remove the remaining material.
4. If required, attach the optional `CMP-ENC-FOOT` feet to the underside of the base plate.
5. Identify the top and bottom of each `PRT-ENC-002` pillar.
6. Insert the `FST-NUT-M5-HEX` nuts into the lower nut seats. Place each pillar on a flat, solid surface and press the nuts fully into place.

> **Caution:** Never brace the pillar against your hand or body while pressing the nuts into place.

### 1.2 Attach the pillars to the base

1. Position one `PRT-ENC-002` pillar at each corner of `PRT-ENC-001`.
2. Orient the pillar grooves toward the corresponding wall positions.
3. Align the pillar mounting holes with the holes in the base plate.
4. Insert the `FST-M5X50` screws through the base and into the captive `FST-NUT-M5-HEX` nuts.
5. Start every screw by hand before using `TOL-HEXKEY-4MM`.
6. Tighten gradually until each pillar is firmly seated against the base.

> **Caution:** Do not force a screw that does not engage freely. Remove it and correct the alignment to avoid cross-threading.

> **Caution:** Do not overtighten against the PMMA base plate.

## 2. Wall installation

The enclosure walls are formed by sliding acrylic panels vertically into the grooves of the support pillars. Together, the four walls define the behavioral enclosure and provide mounting interfaces for the submodules.

In the configuration shown here:

- `PRT-ENC-003` and `PRT-ENC-004` form the wall supporting the feeder module;
- `PRT-ENC-005` and `PRT-ENC-006` form the opposite wall supporting the two screen modules;
- `PRT-ENC-007` and `PRT-ENC-008` form the lateral wall supporting the master module;
- `PRT-ENC-009` and `PRT-ENC-010` form the lateral wall containing the access door;
- `PRT-ENC-011` is the door panel.

Each wall is made from **two matching acrylic panels** installed together in the pillar grooves and secured with M3 fasteners.

### 2.1 Prepare the wall panels

1. Inspect all wall panels for cracks, scratches, or other visible damage.
2. Check that all holes, slots, and panel edges are free of debris.
3. Identify the inward-facing surface of each panel.
4. Pair the two matching panels that form each wall.
5. Identify the intended position and orientation of each wall.
6. Confirm that all module openings and mounting features face the correct direction.

> **Note:** Acrylic panels typically have one glossy surface and one matte, non-reflective surface. Install the panels with the matte surface facing the inside of the behavioral enclosure. This reduces internal reflections that could disturb the animal or interfere with video-based tracking and identification.

**Checkpoint:** All panels are clean and undamaged, each wall pair is identified, and the matte surfaces face inward.

### 2.2 Install the wall panels

1. Begin with the feeder wall pair `PRT-ENC-003` and `PRT-ENC-004`.
2. Align the vertical edges of the first panel with the grooves in the two adjacent `PRT-ENC-002` pillars.
3. Slide the panel downward until fully seated.
4. Slide the matching second panel into the same wall position.
5. Confirm that both panels are fully seated and their fastening holes are aligned.
6. Repeat for the screen wall pair `PRT-ENC-005` / `PRT-ENC-006` and the master-module wall pair `PRT-ENC-007` / `PRT-ENC-008`.
7. Leave the door wall pair `PRT-ENC-009` / `PRT-ENC-010` and the door `PRT-ENC-011` for Section 3.

> **Caution:** Do not force a panel into the pillar grooves. If it does not slide freely, remove it and check the alignment and groove clearance before trying again.

**Checkpoint:** The feeder, screen, and master-module wall assemblies are fully seated, correctly oriented, and captured in the pillar grooves.

### 2.3 Secure the wall panels

1. Confirm that both panels forming each wall are fully seated.
2. Align the fastening holes through the two panels.
3. Insert the `FST-M3X8` screws through the specified fastening positions.
4. Install one `FST-NUT-M3-HEX` on each screw.
5. Start all fasteners by hand before tightening.
6. Tighten evenly until the panels are held firmly together.
7. Check that the panels remain seated in the pillar grooves.

> **Caution:** Do not overtighten fasteners against PMMA. Excessive clamping force can crack the acrylic around the mounting holes.

**Checkpoint:** The three fixed wall assemblies are secure, with no visible cracking, deformation, or looseness.

## 3. Door assembly

### 3.1 Install the door wall

1. Pair `PRT-ENC-009` and `PRT-ENC-010` with the matte surfaces facing inward.
2. Orient the light-blocking overlap correctly.
3. Slide both panels into the corresponding pillar grooves until fully seated.
4. Align and secure the panels using the specified `FST-M3X8` screws and `FST-NUT-M3-HEX` nuts.

**Checkpoint:** The door wall is fully seated, aligned, and secure.

### 3.2 Install the door and hinges

1. Position the `PRT-ENC-011` door panel in the door opening.
2. Position the two `FST-HIN` hinges and align the mounting holes.
3. Use `FST-M3X8` fasteners on the thinner stack and `FST-M3X10` fasteners on the thicker stack.
4. Install the corresponding `FST-NUT-M3-HEX` nuts.
5. Tighten until secure without stressing the acrylic.
6. Check that the door moves freely.

**Checkpoint:** The door is aligned and opens and closes without binding.

### 3.3 Install the door button and locking element

1. Insert one `FST-INS-M3-BRASS` threaded insert into the `PRT-ENC-013` door button.
2. Install `PRT-ENC-013` using the specified `FST-M3X8` hardware.
3. Install and align the `PRT-ENC-012` door locking element.
4. Close the door and verify that the locking element engages correctly.

**Checkpoint:** The door button is secure and the locking element holds the door closed reliably.

## 4. Validate the door

1. Confirm that the `PRT-ENC-009` and `PRT-ENC-010` door-wall panels are fully seated in the pillar grooves.
2. Confirm that their fastening holes remain aligned and secure.
3. Open and close the `PRT-ENC-011` door several times.
4. Check that the door moves freely without rubbing, binding, or shifting.
5. Confirm that the `PRT-ENC-012` locking element engages and releases smoothly.
6. Check that hinges, screw heads, nuts, and other hardware do not create sharp or accessible protrusions inside the enclosure.

**Checkpoint:** The door is aligned, opens and closes smoothly, and locks securely.

## 5. Install the additional modules

1. Mount the completed submodules, such as the feeder, screens, and water bottle mount, onto their corresponding wall panels.
2. For each module, confirm that its `FST-INS-M3-BRASS` mounting inserts are installed and aligned with the wall mounting holes.
3. Secure the modules to the enclosure using `FST-M3X8` M3 × 8 mm screws.
4. Attach the light module to the `PRT-ENC-014` clear top panel using its designated mounting holes.
5. Place the `CMP-ENC-BIN` plastic bin inside the enclosure and slide it fully into position. Confirm that it lies flat.
6. Position the photobeam gate inside the enclosure, resting it on top of the plastic bin.
7. Place the `PRT-ENC-014` clear top panel on top of the enclosure. The panel should hold the photobeam gate in its final position.
8. Confirm that the `FST-NUT-M5-HEX` nuts are correctly seated in the upper nut pockets of the `PRT-ENC-002` support pillars.
9. Align the top panel with the pillar mounting holes and secure it using four `FST-M5X5` fasteners.

> **Caution:** Before securing the top panel, check that the photobeam gate, cables, and other modules are correctly positioned and are not trapped or compressed.

**Checkpoint:** All submodules are securely mounted, the bin and photobeam gate are correctly positioned, and the top panel is fully seated and secured.
