# Validation command-line tool

`micropython/tools/bb_cli.py` lets you **talk to the box from a terminal**: type a short command, the main module turns it into CAN messages, and replies come back as text. It is the quickest way to check that every module is alive and behaves, and to find faults, **without the PC application**.

```{admonition} Requirements
:class: important
- The main module must be deployed with **`CLI_MODE = True`** ({doc}`deploy`). In that mode the PC application cannot connect.
- The PC needs Python with `pyserial` (the `bb_mpy` conda environment has it).
- This tool is a development and validation tool: it is not used during an experiment.
```

## Starting it

```bash
python tools/bb_cli.py                        # interactive prompt (default port /dev/ttyUSB0, 921600 baud)
python tools/bb_cli.py -p COM5                # a different port (Windows)
python tools/bb_cli.py -p /dev/ttyUSB1 -b 921600
python tools/bb_cli.py -c SCAN                # one command, then exit (repeatable)
python tools/bb_cli.py -f my_scenario.txt     # replay a script of commands
python tools/bb_cli.py --list-commands        # print the command reference (no box needed)
```

A script file is a list of commands, one per line; `#` starts a comment and `sleep <seconds>` waits.

## Example session

```text
bb> SCAN
>> SCAN
<< OK SCAN
<< FOUND_FEEDER
<< FOUND_LIGHTING
bb> STATUS FEEDER
<< FEEDER_STATUS_IDLE
bb> DUTY 255 0 0            # white=255, red=0, ir=0
bb> LIGHT ON WHITE
bb> FEED                    # one reward, feeder owns the retries
<< FEEDER_REWARD_1          # pellet present
<< FEEDER_REWARD_0          # pellet taken
bb> REWARD ON               # direct motor control, for maintenance
bb> REWARD OFF
bb> CAN STATUS FEEDER REQ_MODULE 1 0x0A   # raw frame escape hatch
```

The board answers `OK <COMMAND>` when a frame was queued and `ERR <reason>` when the command is wrong. It then forwards the decoded replies it hears on the bus: `FOUND_*`, `*_STATUS_*`, `*_REWARD_*`, `LIGHTING_DUTY_*`, `NOSEPOKE_EVENT_BEAM_*`, `IR_BARRIER_*`, and so on.

## Command reference

Commands are case-insensitive. `[module]` is an optional leading module name (`FEEDER`, `NOSEPOKE`, `SCREEN_LEFT`, `SCREEN_RIGHT`, `LIGHTING`, `IR_BARRIER`, `MAIN`, `GENERIC`, or `ALL`/`BROADCAST`); when you leave it out, the command goes to the module that makes sense for it (shown in the table).

| Command | Default module | What it does |
| --- | --- | --- |
| `SCAN` | broadcast | Every module announces itself (`FOUND_…`) |
| `STATUS [module]` | broadcast | Ask for status: `INIT`, `IDLE`, `ACTIVE` or `ERROR` |
| `RESET [module] [delay_ms]` | broadcast | Reset a module, optionally after a delay |
| `LED [module]` | generic | Toggle the module's CAN LED (identify a board) |
| `FEED [module]` | feeder | Deliver **one reward**; the feeder retries up to 20 times by itself |
| `REWARD [module] ON\|OFF` | feeder | Run the feeder motor directly (maintenance). Stops by itself after 15 s |
| `REWARDSTATUS [module]` | feeder | Read whether a pellet is present |
| `BEAM [module]` | nosepoke | Read the nosepoke beam |
| `BARRIER [module]` | tunnel | Read the infrared beams of the tunnel |
| `PATTERN [module] <id>` | broadcast | Show a pattern on a screen (ids below) |
| `DUTY [module] <white> [red] [ir]` | lighting | Set brightness, each from 0 to 255 |
| `GETDUTY [module]` | lighting | Read the brightness values |
| `LIGHT [module] ON\|OFF [group]` | lighting | Switch a group (`IR`, `RED`, `WHITE`) on or off; `LIGHT OFF` alone switches all off |
| `CAN <prio> <module> <type> <cmd> [bytes…]` | — | Send a raw CAN frame |
| `MODULES` | local | List known module names and numbers |
| `HELP` | local | List the commands |
| `PING` | local | Check that the main module is alive |

`MODULES`, `HELP` and `PING` are answered by the main module itself; no CAN traffic is generated.

### Screen pattern numbers (as accepted by the screen program)

| Id | Pattern |
| ---: | --- |
| 0 | Black |
| 1 | White |
| 2 | Blink |
| 3 | Vertical lines |
| 4 | Horizontal lines |
| 5 | Grid |
| 6 | Diagonal (top-right to bottom-left) |
| 7 | Diagonal (top-left to bottom-right) |

### Raw frames

`CAN <prio> <module> <type> <cmd> [bytes…]` sends an arbitrary frame: *prio* is `ERROR`, `CONTROL`, `EVENT`, `STATUS`, `TELEMETRY` (or 0–4); *type* is `REQ_COMMON`, `RSP_COMMON`, `REQ_MODULE`, `RSP_MODULE` (or 0–3); numbers can be decimal or `0x…` hexadecimal. Details of the identifier layout are in {doc}`can-intermodule-protocol`.

## How it works

The command table lives in `libs/cli_protocol.py` and is imported by **both** the board and the PC tool, so the two sides cannot disagree on the grammar. Each command resolves to an *intent* — the same objects the V2 frontend produces — so the CLI and the application exercise **identical code paths** all the way down to the bus ({doc}`architecture`).

## Troubleshooting the tool

| Symptom | Likely cause |
| --- | --- |
| `pyserial is required` | Install it: `pip install pyserial` |
| Cannot open the port | Wrong port name, or another program holds the port |
| No answer at all | The main module is in V2 mode (`CLI_MODE = False`), or the baud rate does not match (921600) |
| `ERR …` | The command is malformed: see the reason after `ERR` and the table above |
| `SCAN` finds only some modules | Check power and cables; see {doc}`../../troubleshooting` |
