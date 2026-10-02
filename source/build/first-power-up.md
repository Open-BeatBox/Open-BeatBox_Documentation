# First power-up and test

You have built the modules, flashed the boards and installed everything in the enclosure. This page takes you from "it is assembled" to "I know every module works", **without any animal in the box**.

```{admonition} Safety
:class: warning
- Check every connection before applying power; disconnect power before changing anything.
- Keep cables clear of moving parts (the feeder disc) and out of the animal's reach.
- Never power-cycle the system with exposed wiring while an animal is inside.
```

## 1. Visual check

- [ ] Every module is mounted and its housing closed ({doc}`assembly`).
- [ ] All inter-module cables are seated and the connectors are fully pushed in.
- [ ] The 12 V adapter is connected to the main module only.
- [ ] The left and right screen boards are the ones you labelled L and R ({doc}`../hardware/flashing-cards`).

## 2. Put the main module in command-line (CLI) mode

For the first tests the main module must be in **CLI mode**, so you can type commands to it. Check that the main module was deployed with `CLI_MODE = True` ({doc}`../hardware/flashing-cards`, {doc}`../software/firmware/deploy`).

Connect the PC to the main module's serial link (typically a USB-serial adapter on UART0, 921600 baud), and power up.

## 3. Start the test tool

In a terminal, in the `micropython/` folder of the Software repository (conda environment `bb_mpy` active):

```bash
python tools/bb_cli.py
```

You get a prompt `bb>`. If your port is not found, give it explicitly: `python tools/bb_cli.py -p COM5 -b 921600` (Windows) or `-p /dev/ttyUSB0` (Linux).

## 4. Find the modules

Type:

```text
bb> SCAN
```

Each module that is present answers with a line starting with `FOUND_`, for example `FOUND_FEEDER`, `FOUND_LIGHTING`. **Every module you built should appear.** If one is missing, see {doc}`../troubleshooting`.

Ask a module for its status:

```text
bb> STATUS FEEDER
<< FEEDER_STATUS_IDLE
```

`IDLE` means "ready". The other states are `INIT` (starting), `ACTIVE` (busy) and `ERROR`.

## 5. Test each module

| Module | Command to type | What you should see |
| --- | --- | --- |
| Any module | `LED <module>` | The module's CAN LED toggles — proves you are talking to the right board |
| Feeder | `FEED` | The disc turns, a pellet drops, and the feeder reports `FEEDER_REWARD_1` (pellet present), then `FEEDER_REWARD_0` once the pellet is taken |
| Feeder (maintenance) | `REWARD ON` … `REWARD OFF` | The motor runs while on — use briefly, only to check rotation |
| Screens | `PATTERN SCREEN_LEFT <id>` and `PATTERN SCREEN_RIGHT <id>` | The chosen pattern appears on the **correct** screen (ids in {doc}`../software/configuration`) |
| Light curtains / tunnel | `BARRIER` | Reports the beam state; pass your hand through the tunnel and ask again, or watch for `IR_BARRIER_…` events |
| Lighting | `DUTY 255 0 0` then `LIGHT ON WHITE` | The white LEDs light; try `RED` and `IR` too |
| Nosepoke (if fitted) | `BEAM` | Reports whether the beam is broken |

The full list of commands is in {doc}`../software/firmware/cli`, and `python tools/bb_cli.py --list-commands` prints it without needing a box.

## 6. Record the result

Note in your lab book: the hardware revision (V3), the date, the software version, the MicroPython version, and the result of each test. Photograph the final wiring.

## 7. Switch to experiment mode

1. Close the CLI tool.
2. Set `CLI_MODE = False` in `micropython/modules/main_module/main_module.py` and deploy the main module again ({doc}`../software/firmware/deploy`).
3. Install the PC application ({doc}`../software/install`) and do a dry run of stage **S1** with no animal ({doc}`../software/pc-app`).

## Before an animal goes in

- [ ] Every module answered to `SCAN`.
- [ ] A reward was delivered, and the sensor saw it.
- [ ] Both screens show patterns, and a response is detected on each.
- [ ] Lighting switches white, red and infrared.
- [ ] The dry run of S1 produced log files in your experiment folder ({doc}`../software/data-output`).
- [ ] You have followed your institution's animal-welfare procedures.
