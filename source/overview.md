# What is Open-BEATBox?

Open-BEATBox is designed for behavioural neuroscience experiments where short, experimenter-driven testing sessions are a limitation. Instead of taking a mouse out of its cage and into a test room for twenty minutes, the **test comes to the mouse**: the box is attached to (or is) the home cage, and the animal chooses when to take part, at any hour, for days or weeks.

## What the box does

An Open-BEATBox lets a mouse:

1. **walk through a tunnel** to start a trial,
2. **look at two screens** that each show a pattern (for example horizontal lines on one side and vertical lines on the other),
3. **respond** by touching or poking the screen it has learned is the "correct" one,
4. **collect a food pellet** from the feeder and retrieve it with a nosepoke,

while the box **records every event with a timestamp**: tunnel crossings, screen choices, rewards delivered, rewards collected. A computer running the control application decides what happens next and writes the results to CSV files that open in Excel, R or Python.

## Why it matters

- **Less handling, less stress.** The animal is not moved to a test room, which limits stress-related bias.
- **More data per animal.** Continuous access gives many more trials per animal and shows circadian, motivational and learning dynamics that short sessions miss.
- **Reproducibility.** Standard hardware, fixed task timing and automatic logs reduce experimenter variability and make protocols easy to share between laboratories.
- **3Rs.** Richer within-animal datasets can improve statistical power and may reduce the number of animals needed.
- **Open and modular.** Hardware, firmware, software and documentation are all open, and each module (feeder, screens, tunnel, lighting, nosepoke) is a separate unit you can reconfigure.

## What is in the box

Open-BEATBox is made of **modules**, each with its own small circuit board and its own tiny computer (a microcontroller). The modules are connected by a shared cable called a **CAN bus**, and one of them — the **main module** — is the link to your PC.

| Module | What it does for the animal | What it senses or drives |
| --- | --- | --- |
| **Main module** | Nothing directly: it is the "switchboard" between the PC and every other module. Also holds the clock and a memory-card slot. | USB / serial link to the PC, 5 V and 12 V power distribution |
| **Feeder** | Delivers a food pellet | Stepper motor, pellet-detection infrared sensor |
| **Nosepoke** | Lets the animal register a "poke" (for instance to collect the pellet) | Infrared beam |
| **Screens (×2)** | Show the visual stimulus on the left and on the right | 2.8" colour screens, infrared light curtains that detect a response |
| **Tunnel / photobeam gate** | Detects that the animal enters the task area, and in which direction | Pairs of infrared light curtains |
| **Lighting** | Day / night cycle and low-light viewing | White, red and infrared LEDs |

The enclosure is built from laser-cut plexiglass panels and 3D-printed parts, and is assembled with a hex key and basic tools; the screen and sensor boards need some soldering. Details are in {doc}`hardware/index` and {doc}`build/index`.

## Hardware versions

The repository documents two mechanical generations. **V3** is the current design and the one this manual teaches you to build. **V2** (SolidWorks sources) is kept for reference. The electronics in the repository are the V3 module boards. See {doc}`hardware/mechanical`.

## Current status

Open-BEATBox is a working open-source platform with real builds and module-level assembly tutorials. The software is a development version. Cost and build-time figures, final protocol templates and several hardware details are still being validated; {doc}`project/status` keeps the honest list.

## Documentation map

- {doc}`how-it-works` — one trial from the animal to the data file, with a diagram.
- {doc}`getting-started` — the full path from "nothing" to "first experiment running".
- {doc}`build/index` — build your own.
- {doc}`hardware/index` — modules, boards and mechanical parts.
- {doc}`software/index` — the control application, training stages, configuration, data files, firmware and protocol.
- {doc}`troubleshooting` — when something does not behave.
- {doc}`glossary` — plain-language definitions.
