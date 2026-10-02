# Architecture

This page explains how the PC application, the main module and the other modules fit together. It is adapted from `ARCHITECTURE.md` in the Software repository, which remains the developers' reference.

For a plain-language walk-through of one trial, read {doc}`../../how-it-works` first.

## The chain

```text
┌────────────┐   serial    ┌─────────────┐    CAN bus    ┌──────────────────┐
│  host app  │ ◄─────────► │ MAIN module │ ◄───────────► │ peripheral       │
│  (pc_app)  │   UART0     │  (RP2040)   │   11-bit ID   │ modules (RP2040) │
└────────────┘             └─────────────┘               └──────────────────┘
                                                          FEEDER, NOSEPOKE,
                                                          SCREEN_L/R, LIGHTING,
                                                          IR_BARRIER, ...
```

The host application talks to exactly one module, `MAIN`. Every other module is reached over CAN, and `MAIN` is the only translator between the two worlds.

Peripheral modules are **autonomous**: they own their sensors, their timing and their retry logic, and they report state changes on the bus without being polled. `MAIN` **routes**; it does not run the experiment.

## Two host protocols, one core

| Mode | The host speaks | Purpose |
| --- | --- | --- |
| **V2 emulation** (default) | The legacy BB Mega V2 wire protocol | Run the existing application unchanged |
| **CLI** (secondary) | Plain-text commands | Bring-up and validation from a PC, no application needed |

The previous Beatbox generation used an ATmega as the main module, and its protocol was tied to hardware: the application drove TTL output pins and read input pins back as a bitfield. That protocol is **emulated, not reimplemented**: the application sees the same pin words it always did, while the pins themselves are now CAN messages.

CLI mode is a development tool, selected when the board is deployed. It replaces the V2 link, so it is never active during an experiment.

The V2 link is a framed serial protocol with a handshake, sequence numbers and a CRC; its frame format is defined once, in the `beatbox_protocol` package, which both the application and the firmware import so that neither side can drift from the other.

## Intents and events

The two host protocols must not each grow their own copy of the CAN encoding. So `MAIN` is built around two in-process value types that form the only interface between transport-specific code and the CAN core:

- **Intent** — *what to emit on the bus*. It already carries the encoded identifier and payload. It is produced by the CLI parser and by the V2 pin map and consumed by the CAN sender.
- **Event** — *what happened on the bus*. It is produced by a single decoder and fanned out to every frontend.

```text
  many producers            narrow, pure            many consumers
 ┌──────────────┐                                 ┌──────────────┐
 │ cli_protocol │──┐                           ┌──│ CliFrontend  │
 │ bb_v2_map    │──┼── Intent ──► CAN ──► Event ──┤ V2Frontend   │
 │ (future)     │──┘   bb_intents     bb_events   │ (future)     │
 └──────────────┘                                 └──────────────┘
```

Adding a host protocol means adding a frontend plus a mapping table. Changing the CAN layout means touching `bb_intents` and `bb_events`. Neither change propagates past this "waist".

## Layers inside the main module

Each layer translates one representation into the next, owns the layer below it, and reaches upward only through injected callables.

| Layer | Translates | Notes |
| --- | --- | --- |
| `SerialManager` | bytes ⇄ lines | Generic transport; takes a UART |
| `V2WireCodec` | lines ⇄ V2 pin words | Framing, CRC, sequence, handshake; owns the pin-state emulator |
| `V2Frontend` / `CliFrontend` | pins or text ⇄ Intent / Event | Mapping policy only |
| `MainModule` | Intent / Event ⇄ CAN | Owns the frontends, the transport and the CAN manager |

Everything below `main_module.py` is free of hardware imports, so the parsers, decoders, mapping tables and the V2 codec can be tested on an ordinary computer.

## How the pin world maps to the bus (V2 emulation)

| Application pin | Becomes on the bus |
| --- | --- |
| `reward` (level) | Feeder `REWARD_ON` / `REWARD_OFF` (direct motor control) |
| `light`, `red_light` (levels) | Lighting `TURN_ON` / `TURN_OFF` for the white / red group |
| Left and right pattern bits (4 bits each) | Screen `DISPLAY_PATTERN` to the left / right screen |

| Event on the bus | Becomes for the application |
| --- | --- |
| Screen `TOUCH_EVENT` | A pulse on `left_response` / `right_response` |
| Tunnel `BARRIER_EVENT` / status | The tunnel-crossing pins |
| Feeder `REWARD_STATUS` | The `nose_poke` pin (pellet present / taken) |
| Feeder error or error status | The `feed_alert` pin |

```{admonition} To verify on hardware
:class: warning
The pattern identifiers the application sends (a 4-bit code per screen, for example `0xF` for full white) and the pattern numbers the screen program accepts (`0`–`7`) are defined in different places. Reading the code, they do not appear to be translated into one another; confirm with a real screen before relying on a particular pattern. See {doc}`../../project/status`.
```

## Repository layout (Software)

```text
Open-BeatBox_Software/
├── pc_app/                  host application (PC)
├── micropython/             module firmware
│   ├── libs/                shared libraries (CAN, serial, CLI grammar, pin map)
│   ├── modules/             one program per module role
│   │   └── main_module/     the main module and its protocol layers (intents, events, V2)
│   ├── tools/               bb_cli.py, the validation client
│   ├── tests/               host-side tests (run on a PC)
│   └── deploy_module.py     copies a module and its dependencies to a board
├── ARCHITECTURE.md
└── README.md
```

Where to read next: the CAN specification ({doc}`can-intermodule-protocol`), the command grammar ({doc}`cli`), the workflow ({doc}`deploy`) and {doc}`../development`.
