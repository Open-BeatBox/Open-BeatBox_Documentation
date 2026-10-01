# Firmware

The **firmware** is the program inside each module's microcontroller. It reads the module's sensors, drives its motor, screen or LEDs, and exchanges messages with the other modules on the CAN bus. In Open-BEATBox it is written in **MicroPython** and runs on the **RP2040** chip.

```{admonition} Where is the firmware published?
:class: important
- **The firmware source is in the Software repository**, in [`micropython/`](https://github.com/Open-BeatBox/Open-BeatBox_Software/tree/main/micropython), together with the PC application.
- The separate [Open-BeatBox_Firmware](https://github.com/Open-BeatBox/Open-BeatBox_Firmware) repository (licence GPL-3.0) is **reserved for stand-alone firmware releases** and currently holds only its licence and README: *no firmware source has been published there yet*.
- An earlier CircuitPython attempt is kept in `circuitpython/` in the Software repository. It is superseded by the MicroPython version and should not be used for a new build.
```

```{toctree}
:maxdepth: 2
:hidden:

architecture
deploy
cli
can-intermodule-protocol
```

## What you will find here

| Page | For whom | What it covers |
| --- | --- | --- |
| {doc}`architecture` | Anyone curious | How the PC, the main module and the other modules fit together; the two host protocols; what "intents" and "events" are |
| {doc}`deploy` | Builders | Flashing MicroPython, deploying a module, operating modes, third-party libraries |
| {doc}`cli` | Builders and developers | The command-line tool to test every module without the PC application |
| {doc}`can-intermodule-protocol` | Developers | The complete CAN message specification |

## Module programs

Each module type has its own program in `micropython/modules/`. All of them are built on a shared base class that handles the CAN bus, module identity and status.

| Module | Program | What it does |
| --- | --- | --- |
| Main | `main_module.py` | Talks to the PC on UART0 and forwards to CAN; scans for modules |
| Feeder | `feeder.py` | Drives the stepper motor, watches the pellet sensor, reports pellet presence |
| Nosepoke | `nosepoke.py` | Reports nose-poke beam breaks |
| Screens | `screenmodule.py` | Draws patterns on the TFT screen; reports responses |
| Lighting | `lighting.py` | Controls white, red and infrared LED groups and their brightness |
| Tunnel | `ir_barrier.py` | Reads the infrared beams, debounces them, reports events with the beam number |
| *(development)* | `blinky.py`, `can_dummy_tx.py`, `can_dummy_rx.py`, `communicator.py` | Bring-up and test programs |

The shared libraries are in `micropython/libs/`: the CAN identifier packing and command tables (`can_protocol.py`), the module base class (`beatbox_module.py`), the CAN manager (`can_manager.py`), the pin assignments per board (`bb_pin_map.py`), and the host-protocol layers used by the main module.

## Common behaviour of all modules

- **Identity.** Every module has a name and a number (for example `FEEDER`, `0x2`).
- **Status.** Each module is in one of four states: `INIT` (0), `IDLE` (1), `ACTIVE` (2), `ERROR` (3).
- **Discovery.** A broadcast `SCAN` makes every module announce itself.
- **Autonomy.** Modules report events on their own, without being polled.
- **Reset.** A module can be reset remotely, with an optional delay.
- **Status LED.** A CAN LED can be toggled remotely, to identify a board.

## Hardware base

The firmware was developed on the **Adafruit Feather RP2040** (CAN variant) as the reference board, and the pin assignments (`bb_pin_map.py`) use its pin names. The Open-BEATBox boards use the same RP2040 with an MCP25625 CAN controller; a different board or pinout needs a custom MicroPython build or a new pin-map entry.

## Known limitations

See the roadmap in the Software repository's `ARCHITECTURE.md` and {doc}`../../project/status`: handshake reliability, dropped CAN messages under high load, MicroPython performance under heavy event rates, missing on-board log storage, and naming inherited from the previous generation ("V2", "bbv2").
