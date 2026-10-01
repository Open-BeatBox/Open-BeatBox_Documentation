# Developing the software

For contributors who want to change the PC application or the firmware. Read {doc}`firmware/architecture` first.

## Get the code

```bash
git clone --recurse-submodules https://github.com/Open-BeatBox/Open-BeatBox_Software.git
cd Open-BeatBox_Software
```

Branches: `main` is the integration branch; `mock_gui` holds an early, hardware-free `tkinter` mock-up of the interface, **deprecated**, kept for reference.

## Repository map

| Path | What it is |
| --- | --- |
| `pc_app/beatbox/gui/` | Qt interface: main window (`arduino_control_app.py`), one widget per box (`bb_device_widget.py`), hardware panel, stage panels, broadcast controller, summary cards |
| `pc_app/beatbox/experiment_managers/` | One state machine per stage (`s1.py` … `s4.py`), the base class, the CSV loggers, the phase and type definitions, the stage registry |
| `pc_app/beatbox/comm/` | Serial communication with the main module (`serial_com.py`), the pin table loader |
| `pc_app/beatbox/config/` | `experiment.cfg`, `pins_config.cfg`, validation specs |
| `pc_app/tests/` | Tests with a fake box (no hardware) |
| `micropython/modules/` | One program per module role |
| `micropython/libs/` | Shared libraries and the main module's protocol layers |
| `micropython/tools/bb_cli.py` | The validation command-line client |
| `micropython/tests/` | Host-side tests of the protocol layers |
| `micropython/deploy_module.py` | Deployment script |

## How a stage works (PC application)

Each stage is a **state machine**. A table maps every *phase* to what happens on entering it, the next phase, an optional timeout, which sensor edges matter and a function that decides the route. Adding a stage means subclassing the previous one, overriding the table entries that change, adding a configuration section and specification, and registering it in `registry.py` (stage classes and the stage order) and in the panel factory (`stage_panels.py`).

The GUI is a thin skin: it displays what the experiment manager emits through signals. Several design notes are in `pc_app/beatbox/todo.md` (moving more decoding from the GUI to the managers, removing duplicated pin-config objects, re-enabling the sequence-number check).

## Running the tests

PC application (needs the dev extras; no hardware):

```bash
cd pc_app
pip install -e ".[dev]"
pytest
```

Firmware protocol layers (run on an ordinary Python):

```bash
cd micropython
python -m pytest tests/ -q
```

Tests that exercise real boards (`timing_benchmarking/`, parts of `tests/`) are not stable yet.

## Conventions that matter

- Keep everything under `main_module.py` free of `machine` and `canio` imports so it can be tested on a PC.
- Shared firmware code must run on **both** MicroPython and CPython: no 3.10+ typing syntax, no `typing` import.
- Compare ticks with `bb_ticks.ticks_diff`.
- Interrupt handlers set a flag only.
- One CAN encoding: add commands in `can_protocol.py`, intents in `bb_intents.py`, events in `bb_events.py`, and mapping tables in the V2/CLI frontends. Update the specification ({doc}`firmware/can-intermodule-protocol`) in the same change.
- The pin table in the PC application and the firmware's V2 emulation must agree (a known duplication).

## Roadmap (from the repository)

Roughly in order of priority:

1. Fix the application handshake that sometimes fails inadvertently.
2. Investigate dropped CAN messages in the main module when many arrive (for example the replies to `SCAN`).
3. Evaluate and improve MicroPython performance under load (Viper and native code for hot paths; interrupt-driven CAN; debounce).
4. Graph plotting in the PC application.
5. Log storage in the main module and more consistent logging.
6. Clean up the repository structure.
7. Retire previous-generation names ("V2", "bbv2") where appropriate.

See {doc}`../project/status` for the full list of open points.

## Contributing

Open an issue first for larger changes. See {doc}`../contributing` for the repositories, licensing and the review process.
