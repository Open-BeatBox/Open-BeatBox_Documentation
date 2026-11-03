# Flashing the module boards

Every Open-BEATBox module has a small computer (an RP2040 microcontroller) that runs the **firmware**. A new board has no firmware, so it does nothing. This page shows how to put the firmware on each board.

**Do this before the boards are installed in their housings**: the USB connector and the buttons are easy to reach on a bare board and hard to reach later, and you can check each board on its own.

```{admonition} You do not need to be a programmer
:class: tip
Flashing is two short operations per board: (1) drag one file onto a USB drive, then (2) run one command. The commands are copied from this page. If a step fails, see {doc}`../troubleshooting`.
```

```{admonition} Read this first — current limitation
:class: warning
The deployment script copies several third-party libraries (CAN driver, screen driver, LED driver) and the host-protocol package from `micropython/libs/`. In the public Software repository these folders are **not yet populated**, so a fresh clone cannot deploy a module until they are added. This is being resolved ({doc}`../project/status`). Until then, ask the Open-BEATBox team for a complete copy of `micropython/libs/`, or add the libraries yourself (see {doc}`../software/firmware/deploy`).
```

## What you need

- A computer (Windows, macOS or Linux) with **Python 3.11 or newer** — installing it with [conda](https://docs.conda.io/) is the simplest way.
- A **USB data cable** (not a charge-only cable) that fits your board.
- The **Software repository** on your computer: [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software) (`git clone --recurse-submodules …`). A *Download ZIP* or a release archive does not contain the two libraries kept as submodules (`beatbox-protocol` and the screen driver); the Software README lists how to fetch them.
- The **MicroPython** file for the RP2040 boards, a `.uf2` file from [micropython.org/download](https://micropython.org/download/). The firmware was developed on the *Adafruit Feather RP2040* build (`ADAFRUIT_FEATHER_RP2040-20260406-v1.28.0.uf2` was the one in use), which is compatible with the custom boards.

## One-time setup on your computer

Open a terminal in the `micropython/` folder of the Software repository and run:

```bash
conda env create -f environment.yml
conda activate bb_mpy
pip install mpremote
```

`mpremote` is the free tool that copies files to a MicroPython board. (It is not included in `environment.yml`.)

## Step 1 — Install MicroPython on the board

1. Hold the **BOOT** button on the board and plug in the USB cable (or press **RESET** while holding BOOT). Release the button.
2. A drive named **RPI-RP2** appears on your computer.
3. **Drag the `.uf2` file onto that drive.** The board reboots by itself and the drive disappears; the board is now a USB serial device.

If the drive does not appear, see *Troubleshooting*.

## Step 2 — Load the Open-BEATBox program

Each module type has its own program. Choose the row for the board in your hand:

| Board | Program to deploy | Notes |
| --- | --- | --- |
| Main module (`BB_RPI_shield_V1`) | `main_module` | Mode: see below |
| Feeder (`BB_feeder_main_V1`) | `feeder` | |
| Nosepoke (`BB_nosepoke_V1`) | `nosepoke` | |
| Screen (`BB_screen_main_V1`) | `screenmodule` | **Left or right: see below** |
| Lighting (`BB_lighting_V1`) | `lighting` | |
| Tunnel (`BB_tunnel_V1`) | `ir_barrier` | |

The two sensor-only boards (the infrared light curtains and the feeder IR barrier) do not appear in the deployment list: the firmware reads them through the module board they are cabled to.

First check what the command would do (nothing is copied):

```bash
python deploy_module.py feeder --dry-run
```

Then deploy (replace `feeder` with the program for your board):

```bash
python deploy_module.py feeder --as-main --port auto
```

`--as-main` installs the program so that it **starts by itself every time the board is powered**. `--port auto` finds the board.

````{admonition} Two modules need one extra decision
:class: important
**Screens — left or right.** The same program serves both screens, and each must announce a different address on the bus. The program ships set to the **right** screen. Before deploying to the **left** screen, open `micropython/modules/screenmodule.py`, and in the last lines change `ScreenModule(module_name="SCREEN_RIGHT")` to `ScreenModule(module_name="SCREEN_LEFT")`; change it back for the right one. Label the boards "L" and "R" right away. Two boards with the same address will confuse the system.

**Main module — which mode?** Open `micropython/modules/main_module/main_module.py`. The line `CLI_MODE = False` (default) makes the board speak to the PC application. Set `CLI_MODE = True` while you **test** the box with the command-line tool ({doc}`../software/firmware/cli`), then set it back to `False` and deploy again before running experiments. See {doc}`../software/firmware/deploy`.
````

If the script stops half-way, press the board's reset button (or unplug and replug it) and run the same command again.

## Step 3 — Check the board

Open the board's text console (called the REPL):

```bash
mpremote
```

On start-up the board prints a line like `Module initialized: NAME=FEEDER, ID=2`. If you see this, the program is running and the board has the right identity. Press `Ctrl+X` to leave.

Then **label the board** (module name) before it goes into its housing.

## Recommended order for a complete box

1. Flash all boards (this page), labelling the left and right screen boards.
2. Assemble each module ({doc}`../build/assembly`).
3. Install the modules and connect them.
4. Power up and test with `SCAN` ({doc}`../build/first-power-up`).

## Updating firmware later

To update a module, repeat Step 2 only (no need to reinstall MicroPython). Note the software version you deployed in your lab notebook so that your data can be traced to the exact firmware. Installing a new MicroPython `.uf2` may erase the files on the board, so deploy the program again afterwards.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| No **RPI-RP2** drive | Use a data cable. Hold BOOT while plugging in. Try another USB port. |
| `mpremote` not found | `pip install mpremote` inside the activated `bb_mpy` environment. |
| Script says dependency files are missing | The libraries in `micropython/libs/` are missing — see the warning at the top. |
| Script fails half-way | Reset the board and run the command again. |
| Board does nothing after deployment | Deploy with `--as-main`. Open `mpremote` and read the error message. |
| `deploy_module.py: Unknown module` | Check the name in the table above (for example `screenmodule`, with no space or dash). |
