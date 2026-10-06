# Inter-module CAN protocol

This is the **specification of the messages** that the main module and the peripheral modules exchange on the CAN bus. It is the reference for anyone writing firmware or a new module, or debugging the bus. If you only want to *use* the box, you do not need it: see {doc}`cli` and {doc}`../pc-app`.

```{warning}
This protocol is under active development and may change as the firmware evolves. The specification below is the Software repository document `micropython/beatbox_intermodule_protocol.MD`; section 8 lists where the **current code differs** from it. Record the software version when you integrate with it.
```

## In plain words

- **CAN** is a two-wire network on which every message is broadcast to every module. Each message carries an **11-bit identifier** and **0 to 8 bytes of data**.
- The identifier says **how urgent** the message is, **which module** it concerns, **what kind** of message it is, and **which command** it is. Modules ignore messages that are not for them.
- When two modules speak at once, the one with the **lower identifier wins** and the other waits, so urgent messages (errors) come first.
- Modules **announce events by themselves** (a response on a screen, a pellet detected, a beam broken); the host does not have to ask repeatedly.

## 1) Identifier layout (11-bit standard CAN)

Open-BEATBox uses standard 11-bit CAN IDs.

### 1.1 Field ordering (MSB -> LSB)

| Bits  | Size | Field  | Meaning |
|-------|------|--------|---------|
| 10..8 | 3    | PRIO   | Arbitration priority class (`0` highest) |
| 7..4  | 4    | MODULE | Target module for request, source module for response |
| 3..2  | 2    | TYPE   | Message class and direction |
| 1..0  | 2    | CMD    | Command index inside the selected TYPE namespace |

Once a module is selected by `MODULE`, the message meaning is described by 3 protocol fields: `PRIO`, `TYPE`, `CMD` (plus payload).

Payload is 0..8 bytes. RTR is not used.

### 1.2 Encoding formula

`CAN_ID = (PRIO << 8) | (MODULE << 4) | (TYPE << 2) | CMD`

## 2) Global dictionaries

### 2.1 Priority classes (`PRIO`)

| PRIO | Class         | Typical usage |
|------|---------------|---------------|
| 000  | P0 highest    | Critical errors, safety urgent |
| 001  | P1 high       | Control commands (start/stop/reset/reward) |
| 010  | P2 medium     | Real-time events (nosepoke, touch, barrier edge) |
| 011  | P3 normal     | Status and ACK traffic |
| 100  | P4 background | Telemetry / periodic reporting |
| 101..111 | Reserved  | Future use |

### 2.2 Type classes (`TYPE`)

| TYPE | Meaning |
|------|---------|
| 00   | Common request |
| 01   | Common response |
| 10   | Module-specific request |
| 11   | Module-specific response |

### 2.3 Module IDs (`MODULE`)

| Module            | Value |
|-------------------|-------|
| GENERIC           | 0x0 |
| MAIN              | 0x1 |
| FEEDER            | 0x2 |
| NOSEPOKE          | 0x3 |
| SCREEN_LEFT       | 0x4 |
| SCREEN_RIGHT      | 0x5 |
| LIGHTING          | 0x6 |
| IR_BARRIER        | 0x7 |
| BROADCAST target  | 0xF |

No response may use `MODULE=0xF`.

## 3) Common namespace (`TYPE=00` / `TYPE=01`)

`CMD` values are global in this namespace.

| TYPE | CMD | Name       | Direction | Default PRIO | Payload |
|------|-----|------------|-----------|--------------|---------|
| 00   | 00  | SCAN       | Request   | P3           | none |
| 01   | 00  | SCAN_REPLY | Response  | P3           | `status_code:uint8` |
| 00   | 01  | GET_STATUS | Request   | P3           | none |
| 01   | 01  | STATUS     | Response  | P3           | `status_code:uint8` |
| 01   | 10  | ERROR      | Response  | P0           | `error_code:uint8` (+ optional module-specific context bytes) |
| 00   | 11  | RESET      | Request   | P1           | `delay_ms:uint16` big-endian |

Modules may append context bytes after `error_code`. Receivers must tolerate an
`ERROR` payload longer than one byte. See section 4.1 for the feeder case.

Status values:
- `0`: INIT
- `1`: IDLE
- `2`: ACTIVE
- `3`: ERROR

## 4) Module-specific namespace (`TYPE=10` / `TYPE=11`)

`CMD` is module-local in this namespace.

### 4.0 Generic (`MODULE=0x0`)

| TYPE | CMD | Name               | Direction | Default PRIO | Payload |
|------|-----|--------------------|-----------|--------------|---------|
| 10   | 00  | TOGGLE_CAN_LED     | Request   | P1           | none |
| 11   | 00  | CAN_LED_STATE      | Response  | P3           | `state:uint8` (`0` off, `1` on, `255` unknown) |
| 11   | 01  | USER_BUTTON_EVENT  | Response  | P2           | `pressed:uint8` (`1` pressed) |

### 4.1 Feeder (`MODULE=0x2`)

| TYPE | CMD | Name              | Direction | Default PRIO | Payload |
|------|-----|-------------------|-----------|--------------|---------|
| 10   | 00  | GET_REWARD_STATUS | Request   | P1           | none |
| 10   | 01  | REQUEST_REWARD    | Request   | P1           | none |
| 10   | 02  | REQUEST_ON        | Request   | P1           | none |
| 10   | 03  | REQUEST_OFF       | Request   | P1           | none |
| 11   | 00  | REWARD_STATUS     | Response  | P3           | `attempts:uint8` (`1..20`) |

`REQUEST_REWARD` must be addressed to `MODULE=0x2`; the feeder ignores it on
`BROADCAST`, so a reward is never delivered by accident.

#### Delivery sequence

One reward is a twentieth of a revolution of the feeder disc. Pellet arrival is
detected by an IR barrier interrupt local to the feeder module, and is not
visible on the bus.

1. Main sends `REQUEST_REWARD`. The feeder switches to `ACTIVE` and starts
   turning. A second `REQUEST_REWARD` received while a delivery is running is
   ignored; poll `GET_STATUS` to observe progress.
2. The feeder turns 1/20 revolution, then waits up to 500 ms for the pellet.
3. If no pellet is detected, it retries from step 2, up to 20 attempts total
   (one full revolution of the disc).
4. On detection the motor stops immediately, the module returns to `IDLE` and
   sends `REWARD_STATUS`. The payload reports how many attempts were needed:
   `1` on first try, up to `20`.

A reward therefore completes in about 500 ms in the nominal case, and can take
up to ~10 s before being reported as failed. Main must not assume a fixed
latency between `REQUEST_REWARD` and `REWARD_STATUS`.

An `attempts` value consistently greater than `1` indicates a feeder running low
or a disc starting to jam, and is worth logging as a health metric.

#### Delivery failure

If the 20 attempts elapse without a pellet, the feeder sends the common `ERROR`
response (`TYPE=01`, `CMD=10`, `P0`) instead of `REWARD_STATUS`, and stays in
`ERROR` status until the next successful reward.

The error payload extends the generic `error_code:uint8` form with the command
that failed and the number of attempts made:

| Byte | Meaning |
|------|---------|
| 0    | `error_code:uint8` = failing command, `0x01` for `REQUEST_REWARD` |
| 1    | `attempts:uint8` = attempts made before giving up |

No successful `REWARD_STATUS` is emitted in this case. A new `REQUEST_REWARD` is
accepted while the module is in `ERROR`, so main can retry after refilling.

### 4.2 Nosepoke (`MODULE=0x3`)

| TYPE | CMD | Name            | Direction | Default PRIO | Payload |
|------|-----|-----------------|-----------|--------------|---------|
| 10   | 00  | GET_BEAM_STATUS | Request   | P3           | none |
| 11   | 00  | BEAM_STATUS     | Response  | P3           | `beam:uint8` (`0` clear, `1` broken) |
| 11   | 01  | BEAM_EVENT      | Response  | P2           | `beam:uint8` (`1` when poke event detected) |

### 4.3 Screen left/right (`MODULE=0x4` / `0x5`)

Screen side is encoded by module ID, so payload has no side field.

| TYPE | CMD | Name                | Direction | Default PRIO | Payload |
|------|-----|---------------------|-----------|--------------|---------|
| 10   | 00  | DISPLAY_PATTERN     | Request   | P1           | `pattern_id:uint8` |
| 11   | 00  | DISPLAY_PATTERN_ACK | Response  | P3           | `pattern_id:uint8` |
| 11   | 01  | TOUCH_EVENT         | Response  | P2           | `touch:uint8` (`1` touched) |

### 4.4 Lighting (`MODULE=0x6`)

| TYPE | CMD | Name           | Direction | Default PRIO | Payload |
|------|-----|----------------|-----------|--------------|---------|
| 10   | 00  | SET_DUTY       | Request   | P1           | `white:uint8, red:uint8, ir:uint8` |
| 11   | 00  | SET_DUTY_ACK   | Response  | P3           | `white:uint8, red:uint8, ir:uint8` |
| 10   | 01  | GET_DUTY       | Request   | P3           | none |
| 11   | 01  | DUTY_STATUS    | Response  | P3           | `white:uint8, red:uint8, ir:uint8` |
| 10   | 10  | TURN_ON_GROUP  | Request   | P1           | `group:uint8` (`0` IR, `1` RED, `2` WHITE) |
| 10   | 11  | TURN_OFF       | Request   | P1           | optional `group:uint8` (empty = all) |

### 4.5 IR barrier (`MODULE=0x7`)

| TYPE | CMD | Name               | Direction | Default PRIO | Payload |
|------|-----|--------------------|-----------|--------------|---------|
| 10   | 00  | GET_BARRIER_STATUS | Request   | P3           | none |
| 11   | 00  | BARRIER_STATUS     | Response  | P3           | `barrier:uint8` (`0` clear, `1` blocked) |
| 11   | 01  | BARRIER_EVENT      | Response  | P2           | `barrier:uint8` (`1` on edge event) |

## 5) Arbitration behavior

With `PRIO` in the top bits, arbitration follows functional urgency before module identity:

1. lower `PRIO` wins first,
2. then lower `MODULE`,
3. then lower `TYPE`,
4. then lower `CMD`.

This avoids permanent dominance by low module IDs and matches the target policy: `error > control > event > status/telemetry`.

## 6) Worked examples

- Broadcast scan request (`P3`, `BROADCAST`, common request, `SCAN`):
  - bits: `011 1111 00 00`
- Nosepoke event (`P2`, `NOSEPOKE`, module response, `BEAM_EVENT`):
  - bits: `010 0011 11 01`
- Lighting set duty (`P1`, `LIGHTING`, module request, `SET_DUTY`):
  - bits: `001 0110 10 00`
- Feeder reward request (`P1`, `FEEDER`, module request, `REQUEST_REWARD`):
  - bits: `001 0010 10 01`, ID `0x129`, no payload
- Feeder reward delivered on the third attempt (`P3`, `FEEDER`, module response,
  `REWARD_STATUS`):
  - bits: `011 0010 11 00`, ID `0x32C`, payload `03`
- Feeder delivery failure after 20 attempts (`P0`, `FEEDER`, common response,
  `ERROR`):
  - bits: `000 0010 01 10`, ID `0x026`, payload `01 14`

## 7) Capacity note

This layout provides `2` command bits (`CMD=0..3`) per TYPE namespace.
If a module later needs more than 4 module-specific operations, use either:

- one `CMD` value as a payload sub-opcode container, or
- a protocol v2 based on 29-bit IDs.

## 8) Where the current code differs from this specification

The following points were found by comparing this specification with the module programs in `micropython/modules/` and `micropython/libs/` of the Software repository (branch `main`, after the GitLab sync of 1 October 2026). They are given so that integrators are not surprised. The developers confirmed on 2 October 2026 that **the firmware is the reference** (its values were tested and adjusted on hardware) and that the specification will be corrected to match it. Until that is done, trust the right-hand column.

| Area | Specification above | Current code |
| --- | --- | --- |
| **Feeder: `REWARD_STATUS` payload** | `attempts:uint8`, sent once at the end of a delivery | The payload is two bytes, `state:uint8` (`1` pellet present, `0` pellet taken) then `attempts:uint8`, sent at `P2` on **every change** of the pellet sensor, and at `P3` in reply to `GET_REWARD_STATUS` |
| **Feeder: direct motor control** | `REQUEST_ON` / `REQUEST_OFF` (`CMD=02` / `03`) | Same codes, named `REWARD_ON` / `REWARD_OFF` in the code and the CLI. The motor stops by itself 15 s after `REWARD_ON` |
| **Feeder: disc fraction per attempt** | One twentieth of a revolution | The constant in `feeder.py` is one **twenty-fifth** (`1/25`), with a comment saying one twentieth |
| **IR barrier events** | `BARRIER_EVENT` payload `barrier:uint8` | Payload is two bytes: `[line_index, state]` (`state` `1` = beam broken, `0` = clear), one event per accepted edge, debounced at 10 ms |
| **IR barrier status** | `BARRIER_STATUS` payload `barrier:uint8` | Payload is `[mask, last_triggered_line]`, with one bit per beam in `mask` (same `CMD=00` response) |
| **Lighting `TURN_OFF`** | Optional group; empty = all | As specified from the CLI. The V2 mapping always sends the group byte, because white and red are driven independently |
| **Screen pattern numbers** | `pattern_id:uint8` (not enumerated) | The screen program accepts `0` black, `1` white, `2` blink, `3` vertical lines, `4` horizontal lines, `5` grid, `6` and `7` the two diagonals. The V2 mapping sends the application's 4-bit pattern code, which uses different numbers (see {doc}`architecture`) |
| **Generic module** | `GENERIC` (`0x0`) commands | Matches: `TOGGLE_CAN_LED`, `USER_BUTTON_EVENT` |

## Related

- {doc}`cli` — send and read these messages from a terminal.
- {doc}`architecture` — how the main module builds and decodes them (intents and events).
- {doc}`deploy` — putting the firmware on the modules.
