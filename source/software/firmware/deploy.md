# Deploying the firmware

This is the reference for installing and updating firmware on the modules. For a step-by-step guide aimed at builders, see {doc}`../../hardware/flashing-cards`.

## Two steps

1. **Install MicroPython** on the RP2040 (once per board).
2. **Deploy the Open-BEATBox program** (each time you update it).

### 1. Install MicroPython

A new board appears as a USB drive named **RPI-RP2** when it is in bootloader mode. Drag the MicroPython `.uf2` file onto it; the board reboots as a USB serial device.

- Build in use: `ADAFRUIT_FEATHER_RP2040-20260406-v1.28.0.uf2`. The custom modules use the Adafruit Feather RP2040 as their base, so that build is compatible. A different base board or pinout needs a custom build or a new entry in `libs/bb_pin_map.py`.
- If the board does not enter bootloader mode: press reset twice quickly while holding BOOT; or from the REPL run `machine.bootloader()`; or from the PC run `mpremote bootloader`.

### 2. Deploy the program

Work in `micropython/` with the conda environment active (`environment.yml`: Python ≥ 3.11, `pyserial`, `pytest`; install `mpremote` with pip).

```bash
python deploy_module.py <module> --dry-run         # show what would be copied
python deploy_module.py <module> --as-main --port auto
```

| `<module>` | Board |
| --- | --- |
| `main_module` | Main module |
| `feeder` | Feeder |
| `nosepoke` | Nosepoke |
| `screenmodule` | Screen (left or right: see below) |
| `lighting` | Lighting |
| `ir_barrier` | Tunnel / photobeam gate |
| `blinky` | Development and bring-up |

`--as-main` installs the module as `main.py`, which MicroPython runs automatically after `boot.py` ([boot sequence](https://docs.micropython.org/en/latest/reference/reset_boot.html#boot-sequence)). Use it for every module you intend to leave running.

The script copies, in order: the host-protocol package, the CAN driver (MCP2515), the shared libraries, the module's extra dependencies, and the module program. The extra dependencies are:

| Module | Extra files |
| --- | --- |
| `main_module` | `serial_manager`, `cli_protocol` (from `libs/`), and `bb_frontends`, `bb_events`, `bb_intents`, `bb_v2_map`, `bb_v2_comm`, `bb_v2_emulator` (from `modules/main_module/`) |
| `screenmodule` | ILI9341 parallel TFT driver (`ILI9341`, `ILI9341_char`, `ILI9341_touch`) |
| `lighting` | PCA9955B LED driver package |

`deploy_module.py` occasionally fails part-way and leaves the board unable to enter raw REPL. Reset it with the button or a power cycle and retry.

### Manual file operations

```bash
mpremote                      # REPL (Ctrl+X to leave)
mpremote ls
mpremote cp path/on/host :path/on/device
mpremote rm :path/on/device
```

## Third-party libraries (read this)

The deployment script copies files from these libraries, expected under `micropython/libs/`:

| Folder expected | Library | Used by |
| --- | --- | --- |
| `beatbox-protocol/` | Host frame format (`BeatBoxMessage`, CRC) — a Git submodule | All modules (and the PC application) |
| `microPython_MCP2515/` | MCP2515/25625 CAN driver | All modules |
| `CircuitPython_PCA9955B/` | PCA9955B LED driver | Lighting |
| `ILI9341-parallel-TFT-driver-for-micropython/` | 8-bit parallel ILI9341 TFT driver | Screens |

```{admonition} Current state of the repository
:class: warning
In the public Software repository, `beatbox-protocol` and `ILI9341-parallel-TFT-driver-for-micropython` are Git submodules: clone with `git clone --recurse-submodules` (or run `git submodule update --init`) to fetch them. The project uses locally modified versions of the other two libraries, so their upstream projects alone are not enough. `microPython_MCP2515` is included as a plain folder (a copy of the upstream driver with the project's changes; MIT licence). `CircuitPython_PCA9955B` is included the same way (a copy of the MicroPython port of the upstream driver, MIT licence), so every module deploys on a fresh clone. The maintainers plan to publish forks of both libraries and turn them back into submodules. The host-protocol package is public at `gitlab.com/icm-institute/rnd-unit-public/rnd_unit_libs/beatbox-protocol`.
```

## Operating modes of the main module

`modules/main_module/main_module.py` has one deploy-time switch:

```python
CLI_MODE = False   # default: legacy V2 emulation
```

| | `CLI_MODE = False` (default) | `CLI_MODE = True` |
| --- | --- | --- |
| Use | Real experiments | Bring-up and validation |
| UART0 carries | The V2 wire protocol: startup and handshake frames, sequence numbers, CRC, pin words in and pin states out | Plain text commands ({doc}`cli`) |
| PC program | The application (`beatbox`) | `tools/bb_cli.py` |
| USB REPL | A human-readable mirror of all CAN traffic | The same |

Wiring in both modes: main-module `UART0` (`tx = GP0`, `rx = GP1`, **921600 baud**) to a USB-serial adapter, typically `/dev/ttyUSB0` (or `COMx` on Windows). Debug logging always stays on the USB REPL, never on the UART.

**Switching mode means editing the line and deploying again.** After testing with the CLI, set `CLI_MODE = False` and redeploy before running experiments.

## The two screens

The same program serves both screens, but its last lines choose the identity:

```python
def main():
    tft.begin()
    screen = ScreenModule(module_name="SCREEN_RIGHT")
    asyncio.run(screen.start_managers())
```

As shipped, this is `SCREEN_RIGHT`. For the left screen, change it to `SCREEN_LEFT` before deploying to that board. Two boards with the same name answer to the same CAN address and will conflict.

## Host-side tests

The protocol layers import no hardware modules, so they run on an ordinary computer:

```bash
python -m pytest tests/ -q
```

This covers identifier packing, the CAN decoder, the command grammar and the V2 mapping. Prefer adding a test here over testing on a board.

## MicroPython constraints worth knowing

- **No 3.10+ typing syntax** in shared code (`str | None`, `list[int]`) and no `typing` import: anything the host tests import must load on both runtimes.
- **Ticks wrap.** `time.ticks_ms/us` roll over (about 17.9 min for µs on the RP2040). Always compare with `bb_ticks.ticks_diff`, never with `-`.
- **Interrupt handlers must be minimal**: set a flag, allocate nothing, never touch the bus. The owning task consumes the flag ([ISR rules](https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules)).
- **Cooperative scheduling.** Every task shares one loop: a blocking sleep in a callback stalls CAN reception and the serial handler too. Defer instead of blocking.
