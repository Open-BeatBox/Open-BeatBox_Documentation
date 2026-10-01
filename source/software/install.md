# Installing the PC application

The PC application (`pc_app/` in the [Software repository](https://github.com/Open-BeatBox/Open-BeatBox_Software)) is a Python program with a graphical interface, built with Qt. This page installs it on your computer.

```{admonition} Status of these instructions
:class: note
They are written from the repository files (`pyproject.toml`, `environment.yml`). The application is a development version; if a step does not work on your system, please open an issue with the error message ({doc}`../troubleshooting`).
```

## What you need

- Windows, macOS or Linux.
- **Git** (to download the code and a protocol library).
- **conda**, for example [Miniconda](https://docs.conda.io/en/latest/miniconda.html). It installs Python and the libraries in an isolated "environment" so nothing else on your computer is affected.
- The box, powered, with the main module connected to the computer (see {doc}`../build/first-power-up`).

## Step by step

Open a terminal (on Windows: *Anaconda Prompt*) and type:

```bash
# 1. Download the software
git clone --recurse-submodules https://github.com/Open-BeatBox/Open-BeatBox_Software.git
cd Open-BeatBox_Software/pc_app

# 2. Create the environment (installs Python 3.11+ and all libraries)
conda env create -f environment.yml

# 3. Activate it (do this each time you open a new terminal)
conda activate beatbox

# 4. Install the application itself, in "editable" mode
pip install -e .
```

**Why "editable" (`-e`)?** The experiment settings are in a plain text file that lives inside the application folder ({doc}`configuration`). An editable install means the file you edit is the file the application reads.

## Start the application

```bash
conda activate beatbox
beatbox
```

A dialog opens asking for the stage and the animal's details ({doc}`pc-app`).

You can also start it with Python directly: `python -m beatbox.gui.arduino_control_app`.

### Start-up options

| Option | Meaning | Default |
| --- | --- | --- |
| `--n-devices N` | Open *N* box panels, to control several boxes from one window | 1 |
| `--n-trials N`, `--inter-trial-interval MS` | Accepted by the program, but the window currently shows the values from the configuration file ({doc}`configuration`); set them there | 20 / 10000 |
| `--with-neopixels` | Show colour-ring controls (for boxes with a NeoPixel ring) | off |
| `--from-config-file PATH` | Load the experiment folder and a few settings from a configuration file | none |
| `--pins-config-file PATH` | Pin table (you should not have to change it) | `~/.beatbox/pins_config.cfg`, otherwise the built-in file |

## Updating

```bash
cd Open-BeatBox_Software
git pull
cd pc_app
conda activate beatbox
pip install -e .
```

Note the version (commit) you ran in your lab notebook, as the software is still evolving.

## Tips for Windows

- If `pip` stops with a *file path too long* error, enable long paths in Windows, or create the environment closer to the root of a drive (for example `C:\bb`).
- The serial port appears as `COM3`, `COM4`, … in the application's port list.
- If the port list is empty, install the driver for your USB-serial adapter (FTDI, CH340 or CP210x) and click **Refresh**.

## Running the tests (optional)

```bash
pip install -e ".[dev]"
pytest
```

The tests use a simulated box; they do not need hardware.
