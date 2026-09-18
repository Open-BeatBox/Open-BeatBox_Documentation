# Hardware Build

Guidance to assemble, wire, and validate an Open-BEATBox cage. Adapt details to your bill of materials (BOM) and enclosure design.

## Bill of materials (BOM)
- Cage and enclosure: printed or machined parts, fasteners, cable glands, mounting hardware, and removable panels for modularity.
- Controller: microcontroller (e.g., ESP32) or single-board computer (e.g., Raspberry Pi) with real-time firmware support.
- Sensors: IR beam breaks or nose-poke sensors, levers, capacitive touch, load cells (optional), environmental sensors (temperature, humidity, light), audio I/O.
- Actuators: pellet or liquid dispenser, indicator LEDs, house lights, speakers/buzzers (if needed).
- Power: regulated supply sized for peak actuator draw; include fusing and protection.
- Connectivity: Wi‑Fi or Ethernet module, USB/serial breakout for setup and streaming.
- Misc: wiring harnesses with labeled connectors, strain relief, cable management, and shielding as required.

> Keep the authoritative BOM in version control; include part numbers, vendors, and acceptable substitutes.

## Assembly steps (high-level)
1. Download CAD, STL, PCB, and wiring diagrams from the Open-BEATBox repository (see Build & Code page).
2. Prepare enclosure panels and mounts; remove burrs/sharp edges.
3. Install controller and breakouts on standoffs; route power separately from signal lines where possible.
4. Mount sensors and actuators; label each connector to match pin assignments.
5. Run wiring harnesses with strain relief; bundle and secure away from chewable areas.
6. Add shielding or twisted pairs for noise-sensitive lines (load cells, analog sensors).
7. Finalize power input (fuse, switch) and verify voltage at each load before connecting animals.

## Wiring and pin mapping
- Maintain a pin map document (CSV or Markdown) with signal names, pin numbers, voltage levels, and connector labels.
- Standardize wire colors per signal type (power, ground, data, control).
- Where possible, use keyed connectors to prevent mis-plugging.

## Firmware/runtime configuration
- Store hardware definitions (pin maps, debounce thresholds, calibration constants) in a tracked config file.
- Provide profiles per build variant (e.g., “IR-only”, “IR + load cell”, “touch nose-poke”).
- Version the firmware/runtime alongside the config so you can trace sessions to exact builds.
- Follow the firmware flashing steps from the Build & Code flow: install toolchain, clone firmware repo, configure for your hardware variant, and flash.

## Calibration and validation
- IR/beam or nose-poke: confirm detection at expected distances; test with known obstructions.
- Reward dispenser: measure and record average delivery per trigger; adjust timing/steps to meet spec.
- Environmental sensors: cross-check against a calibrated reference; set alert thresholds.
- Time sync: verify NTP/RTC; log offsets during validation.
- Run a dry task: simulate events and ensure logs capture timestamps, sensor values, and actuator states.

## Maintenance
- Daily: visual inspection, cable seating, sensor/actuator sanity checks.
- Weekly: clean sensors and actuators, check fasteners, inspect cable strain relief.
- Monthly/after major changes: full calibration pass and pin-map verification.

## Safety notes
- Disconnect power before rewiring.
- Avoid overloading power rails; check total draw during peak actuator use.
- Keep wiring and electronics outside the animal area when feasible.
