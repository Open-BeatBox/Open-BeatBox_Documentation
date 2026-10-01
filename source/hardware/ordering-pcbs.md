# Ordering the circuit boards

The eight board designs ({doc}`pcbs`) are made by a PCB service from the manufacturing files in each board's `production/` folder. The project's files were prepared for **JLCPCB**; other services accept the same Gerber files, but the BOM and pick-and-place files use **LCSC** part numbers, which map directly to JLCPCB's assembly service.

```{admonition} Recommendation
:class: tip
Order **assembled** boards (fabrication + component assembly). Hand-soldering the fine-pitch components of these boards is not recommended.
```

## What you need from each board folder

| File | Used for |
| --- | --- |
| `production/<board>.zip` | **Gerber files**: the board itself. Upload as it is, do not unzip. *(stored with Git LFS)* |
| `production/bom.csv` | Which components go on the board (designator, footprint, quantity, value, LCSC part number) |
| `production/positions.csv` | Pick-and-place: the position and rotation of every component |
| `production/designators.csv` | Reference designators |

If the `.zip` arrives as a tiny text file, you cloned the repository without Git LFS. Download the file from the GitHub web page, or run `git lfs install` and `git lfs pull`.

## Option A — assembled boards (recommended)

1. **Upload** the Gerber `.zip` and check the board preview.
2. **Configure the PCB:** most defaults are fine. You may choose a thickness and colour. A **lead-free HASL** finish is recommended.
3. **Enable PCB assembly** and choose the assembly side(s).
4. **Upload `bom.csv` and `positions.csv`.** Check that every component in the selection table is available.
5. **Verify**: availability, the mapping to LCSC parts, rotations, polarity and connectors. Compare against the board's PDF schematic if in doubt.
6. **Final check:** no missing components, price and lead time. Confirm the quantity (see {doc}`pcbs` for how many of each board).

## Option B — bare boards

Fabrication only, no assembly. Follow steps 1, 2 and the final check above. You then buy the components and solder everything yourself. This is cheaper but needs good soldering skills and equipment.

## Components that need separate handling

- Some connectors may not be offered by the assembly service. Order them separately and solder by hand.
- Parts that are out of stock can sometimes be substituted. **Always double-check polarity and orientation** before confirming the assembly.
- If a non-generic component is unavailable, consult an electronics engineer to choose an equivalent or adapt the design.

## After the boards arrive

- [ ] Count the boards against {doc}`pcbs`.
- [ ] Inspect visually: connectors seated, no solder bridges, correct orientation.
- [ ] **Flash** each board ({doc}`flashing-cards`) before closing it into its housing.
