# Glossary

Plain-language definitions of the terms used across the Open-BEATBox manual.

## The experiment

```{glossary}
Home cage
  The cage where the animals live. Open-BEATBox brings the task into it, so animals are not moved to a testing room.

Operant conditioning
  A kind of learning in which an animal learns that a particular action (touching a screen, poking a hole) leads to a consequence (a food pellet).

Trial
  One attempt at the task: from the start signal (for example entering the tunnel) to the end of the outcome (reward collected or error handled).

Inter-trial interval (ITI)
  The rest period between two trials. Configurable.

Stage (S1, S2, S3, S3.1, S4)
  A level of the training protocol. The animal moves from simple stages to harder ones. See {doc}`software/stages`.

Corrective loop
  After an incorrect choice, the same trial is repeated after a short pause so the animal gets another chance. Not used in stage S3.1.

Learning threshold
  The success rate (for example 0.8 = 80 %) over the last *n* trials that the animal must reach before the stage is considered complete.

Time pressure
  The maximum delay allowed between a correct screen response and collecting the pellet. A slower correct response counts as *invalid*.

Valid / invalid / incorrect response
  *Valid*: correct side and pellet collected in time. *Invalid*: correct side but pellet collected too late. *Incorrect*: wrong side.

Discovery pattern
  A third pattern used in stage S4 that is rewarded only with a given probability, to test exploration.

Pattern
  The image shown on a screen: white, black, horizontal lines, vertical lines, grid, or a diagonal. See {doc}`software/configuration`.
```

## The hardware

```{glossary}
Module
  A self-contained unit of the box with its own circuit board and housing: main, feeder, nosepoke, screen, tunnel, lighting.

Main module
  The module connected to your computer. It passes messages between the PC and every other module. Built on the *BB_RPI_shield* board.

Peripheral module
  Any module other than the main module.

PCB
  Printed circuit board: the green board carrying the electronic components. Open-BEATBox uses eight designs. See {doc}`hardware/pcbs`.

Microcontroller (MCU)
  A very small computer on a chip. Every module has one. Open-BEATBox uses the **RP2040** (the chip of the Raspberry Pi Pico).

CAN bus
  A two-wire network, like those in cars, that carries the messages between modules. In Open-BEATBox each module has a CAN controller (MCP25625). See {doc}`software/firmware/can-intermodule-protocol`.

Photobeam gate / tunnel
  The passage the animal walks through. Pairs of infrared beams detect that it entered and in which direction.

IR light curtain
  A row of infrared beams (pulsed at 38 kHz, which makes it insensitive to room light) that detects when something interrupts it.

Nosepoke
  A hole with an infrared beam that records when the animal pokes its nose in.

Feeder
  The module that delivers food pellets by turning a disc with a stepper motor.

Stepper motor
  A motor that turns in small, precise steps. Used in the feeder.

Gerber files
  The standard files a PCB factory needs to make a board.

BOM
  Bill of materials: the list of every part, quantity and supplier. The *Master BOM* lists all parts for the whole box.

KiCad
  Free, open-source software for designing circuit boards. The hardware files are KiCad projects.

STEP / STL / DXF
  File formats for mechanical parts. STEP: exchange format for CAD. STL: mesh for 3D printing. DXF: outline for laser cutting.

Git LFS
  Git Large File Storage. How big files (`.STEP`, `.zip`) are stored in the Hardware repository.
```

## The firmware and software

```{glossary}
Firmware
  The program that runs inside a module's microcontroller. In Open-BEATBox it is written in MicroPython.

MicroPython
  A version of the Python language that runs on microcontrollers.

UF2
  The file format used to install MicroPython on an RP2040 board by dragging a file onto a USB drive.

Flashing
  Installing firmware (or the MicroPython interpreter) on a board.

Deploying
  Copying the Open-BEATBox program files onto a board that already runs MicroPython.

REPL
  The text prompt of MicroPython, reached over USB. Useful to see what a board is doing.

mpremote
  A free command-line tool that copies files to, and talks to, a MicroPython board.

Host application / PC application
  The program on your computer that runs the experiment (`pc_app/`). Also called the *control application* or *GUI*.

Handshake
  The initial "hello" exchange between the PC application and the main module that confirms they can understand each other.

V2 emulation
  The main module's default mode: it pretends to be the previous-generation Arduino-based controller so the PC application works unchanged.

CLI (command-line interface)
  A text-based way to control the box by typing commands. Open-BEATBox has one for testing modules. See {doc}`software/firmware/cli`.

Intent / Event
  Two internal concepts in the main module: an *intent* is "what to send on the bus", an *event* is "what was heard on the bus".

Frame
  One CAN message. It has an identifier and 0–8 bytes of data.

Priority
  How urgent a CAN message is. Errors beat commands, which beat events, which beat status reports.

CSV
  A plain-text table format (comma-separated values) that opens in Excel, R, Python, or any text editor. The result files are CSV.

conda
  A tool that installs Python and its libraries in an isolated environment, so the application does not interfere with other software.
```
