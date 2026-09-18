# User Guide

Practical steps to deploy, operate, and maintain an Open-BEATBox home-cage behavioral system.

## Open-BEATBox at a glance
- Ecological, automated operant-conditioning and home-cage monitoring for mice with continuous (24/7) access to tasks.
- Typical stack: microcontroller or SBC, environmental/behavioral sensors (IR beam breaks, nosepoke, levers, capacitive touch), actuators (pellet or liquid dispenser, lights), audio I/O, network connectivity, and a data pipeline for experiment logs.
- Streams to a local PC or server via USB or Wi‑Fi; APIs exposed through Python clients and REST/WebSocket interfaces.

## Before you start
- Confirm you have a complete kit (see [Hardware Build](hardware-build.md) for BOM and wiring).
- Prepare network access (wired or Wi‑Fi) and power.
- Install client tools you’ll use to interact with the device (e.g., SSH, serial console, or a web UI if provided).

## Setup checklist
1. Assemble the cage and verify all connections are secure and labeled (see [Hardware Build](hardware-build.md)).
2. Power on with no animals present; confirm baseline sensor readings.
3. Connect to the device (USB/serial, SSH, or web UI) and check firmware version.
4. Configure network, timezone, and storage paths for data logs.
5. Load the initial behavioral task configuration; keep a copy under version control.
6. Run a dry run: trigger sensors manually, observe actuator behavior, and confirm events log to the expected storage or stream as expected.

## Running experiments
1. Prepare the subject and cage (clean bedding, water, food hoppers calibrated).
2. Start the task: launch via CLI/web UI or schedule on boot.
3. Monitor health signals: temperature/humidity, error logs, and network stability.
4. Mark experimental metadata (animal ID, cohort, task version, start time) in the run record.
5. End of session: stop the task, export or sync logs, and note anomalies.

## Daily validation
- Sensor sanity check: light, temperature/humidity, beam breaks or nose-poke sensors respond within expected latency.
- Actuator check: reward delivery and lights activate reliably; no jams in dispensers.
- Storage and sync: ensure logs rotate and offload; verify free space.
- Time sync: confirm NTP or RTC is correct to keep timestamps aligned.

## Safety and welfare
- Never power-cycle with animals inside if wiring is exposed.
- Keep cables secured outside chewable range; use strain relief.
- Avoid sharp edges or protruding components in the cage.
- Document deviations from standard operating procedures.

## Updating firmware/runtime
- Back up current configuration and logs.
- Apply updates in a maintenance window; note firmware/runtime version and commit hash.
- After updating, rerun validation and a short pilot session before resuming production use.

## Troubleshooting quick hits
- **No sensor events**: re-seat connectors, check pin mappings, confirm firmware config, and watch serial logs.
- **Network drops**: test with wired fallback if available; check power stability and Wi‑Fi signal strength.
- **Timestamp drift**: ensure NTP is enabled or sync RTC; avoid offline runs longer than the clock can hold.
- **No rewards dispensed**: inspect hopper/dispenser for jams; test actuator manually; confirm task logic thresholds.

## Data handling
- Keep raw logs immutable; derive analysis-ready tables separately.
- Record task version and configuration alongside each session.
- For multi-cage setups, enforce consistent subject IDs and clock sync across devices.
- Data is typically streamed via USB/Wi‑Fi to a local PC/server and exposed through Python clients or REST/WebSocket APIs; see [Data & Analysis](data-analysis.md) for pipelines and formats.
