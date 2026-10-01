# Software

The Open-BEATBox software has **two halves**, both in the [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software) repository (licence: AGPL-3.0):

| Half | Where it runs | What it does | Folder |
| --- | --- | --- | --- |
| **PC application** | Your computer | Runs the experiment: training stage, trial logic, graphical interface, result files | `pc_app/` |
| **Module firmware** | Inside each module (MicroPython on RP2040) | Reads sensors, drives motors, screens and LEDs, talks on the CAN bus | `micropython/` |

A third, smaller piece, the **validation command-line tool**, lets you test the box from a terminal without the application (`micropython/tools/bb_cli.py`).

```{admonition} Development version
:class: warning
The software is an **ongoing development version**. Interfaces, CAN payloads and the host protocol are still moving, and the repository roadmap lists known issues (handshake reliability, dropped CAN messages under load, performance). Always note the software version you used with your data. See {doc}`../project/status`.
```

## Which page do I need?

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Install the PC application
Python, conda, and the first launch.

{doc}`install`
:::

:::{grid-item-card} Use the application
Connect to the box, choose a stage, enter animal details, start, monitor, stop.

{doc}`pc-app`
:::

:::{grid-item-card} Training stages S1–S4
What the animal does at each stage, what is rewarded, and when a stage is complete.

{doc}`stages`
:::

:::{grid-item-card} Configure experiments
Every parameter of the configuration file, with examples.

{doc}`configuration`
:::

:::{grid-item-card} Your data
Which files are written, what every column means, how to open them.

{doc}`data-output`
:::

:::{grid-item-card} Firmware and protocol
How modules are programmed and how they talk to each other.

{doc}`firmware/index`
:::

:::{grid-item-card} Contribute code
Repository layout, running the tests, coding constraints.

{doc}`development`
:::

::::

```{toctree}
:maxdepth: 2
:hidden:

install
pc-app
stages
configuration
data-output
firmware/index
development
```

## Overview of the flow

```text
 Your PC                                   Inside the box
┌─────────────────────────┐   serial     ┌──────────────┐   CAN bus    ┌───────────────────────┐
│ PC application          │◄────────────►│ MAIN module  │◄────────────►│ feeder · screens      │
│  • stage logic          │  921600 baud │ (firmware)   │              │ tunnel · lighting …   │
│  • GUI                  │              └──────────────┘              │ (firmware in each)    │
│  • CSV logs             │                                            └───────────────────────┘
└─────────────────────────┘
```

For the full story of a trial see {doc}`../how-it-works`.
