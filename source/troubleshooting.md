# Troubleshooting

Start with the symptom you see. The most common causes are listed first. If nothing here helps, open an issue (see the end of this page) and include the information listed there.

```{admonition} Safety first
:class: warning
Disconnect power before touching wiring or changing a board. Do not power-cycle the system with exposed wiring while an animal is inside.
```

## Building and flashing

### A new board does not show up as a USB drive named RPI-RP2

- Use a **data** USB cable, not a charge-only cable.
- Put the board in bootloader mode: hold the **BOOT** button while pressing **RESET** (or powering it), then release. Some boards need *RESET* pressed twice quickly.
- From a board that is already running MicroPython, `machine.bootloader()` in the REPL, or `mpremote bootloader` from your PC, restarts it in bootloader mode.

### The deployment script fails part-way

`deploy_module.py` can occasionally leave a board unable to enter its "raw REPL" (the mode used to copy files). Press the reset button or power-cycle the board, then run the script again. See {doc}`software/firmware/deploy`.

### "Some dependency files are missing" when deploying

The deployment script copies a few third-party libraries by path (CAN driver, LED driver, screen driver, protocol package). These must be present under `micropython/libs/` in the Software repository. If the folders are empty, the repository was cloned without them — see the open point in {doc}`project/status`.

### The board is flashed but the module does nothing

- The module runs the program saved as `main.py`. Deploy with `--as-main` (see {doc}`software/firmware/deploy`).
- Open the REPL (`mpremote`) and look for an error message printed at start-up.

## Connecting

### `SCAN` finds nothing, or only some modules

- Check each module's **power** (5 V and 12 V are distributed from the main module) and the **cables between modules**: a loose connector is the most common cause.
- Each module has a CAN LED; the `LED` command toggles it so you can tell a module is alive.
- Known issue: the main module can drop CAN messages when too many arrive at once (for instance the replies to a broadcast `SCAN`). Run `SCAN` again, or query modules one by one with `STATUS <module>`.

### The PC application cannot connect, or the handshake fails

- Confirm the main module is deployed in **V2 emulation** mode (`CLI_MODE = False`), not CLI mode. In CLI mode it speaks text and the application cannot connect.
- Make sure no other program (a serial terminal, the CLI tool) holds the serial port.
- The application and the main module both use **921600 baud**. If you changed one of them, change the other to match.
- Check the wiring of the serial link between the PC and the main module (see {doc}`software/firmware/index`).
- A failed handshake "inadvertently" is a known item on the roadmap. Restarting the application and power-cycling the main module usually helps.

### The application does not list my port

The application looks for known USB-serial identifiers (Arduino, FTDI, CH340, CP210x). Unplug and re-plug the adapter, and check that your operating system recognises it (device manager on Windows, `ls /dev/ttyUSB*` on Linux).

## During an experiment

### No pellet is delivered

- An empty feeder or a jammed disc is the usual cause. Refill or clear it.
- In an experiment the application tries again every second and shows a **pellet delivery alert** in the hardware panel while it does. If the alert keeps counting, stop and inspect the feeder.
- With the test command `FEED`, the feeder tries up to 20 times (one full turn of the disc, about 10 seconds), then reports an error. A new request is accepted even after an error, so you can refill and retry.
- If a single reward often needs more than one attempt, the feeder is running low or the disc is starting to jam.

### The pellet is delivered but the application does not notice

The pellet sensor (a small infrared photo-interrupter in the feeder) may be misaligned. The assembly tutorial mentions removing a small black locating pin if it stops the sensor lying flat. Check the sensor board seating and the connector.

### A screen stays black, or shows the wrong pattern

- Check the screen's ribbon / cable seating and the backlight.
- Use the CLI `PATTERN <screen> <id>` command to test the screen without the application ({doc}`software/firmware/cli`).
- Pattern identifiers are listed in {doc}`software/configuration`.

### Responses are not detected

- Check the infrared light curtain boards of that screen and the cable.
- Remember that the infrared barrier is sensitive to alignment and to cracked or dirty acrylic. Do not clean laser-cut plexiglass with alcohol ({doc}`build/safety`).

### The application is slow when many events arrive

Known limitation of the current MicroPython firmware under heavy event load. It is on the roadmap ({doc}`project/status`).

### My stage never finishes

The stage is complete only when the success rate over the last *n* trials reaches the learning threshold (in S3 and S4, *on each side*). Look at the left and right performance values in the application and at your `n_trials` and `learning_threshold` values ({doc}`software/configuration`).

## Data

### I cannot find my result files

Files are written in the **experiment folder** you chose with **Select Folder** before pressing *Start Experiment* (the start button stays disabled until you have chosen one). File names contain the animal name, the stage and a timestamp ({doc}`software/data-output`).

### Timestamps look wrong

Event timestamps in the logs are relative to the start of the session. The absolute date and time are in the `date` column and come from the PC's clock — check that it is synchronised.

## Reporting a problem

Open an issue in the repository that matches the problem and include:

- the **hardware revision** (for example V3) and module(s) involved;
- the **software commit** or release, and the MicroPython version;
- what you did, what you expected, what happened;
- for a build problem: the item ID and module ID from the BOM, and a photograph.

| Problem with… | Issue tracker |
| --- | --- |
| Assembly tutorials or BOM | [Open-BeatBox_Documentation](https://github.com/Open-BeatBox/Open-BeatBox_Documentation/issues) |
| CAD, PCB or mechanical files | [Open-BeatBox_Hardware](https://github.com/Open-BeatBox/Open-BeatBox_Hardware/issues) |
| PC application or module firmware | [Open-BeatBox_Software](https://github.com/Open-BeatBox/Open-BeatBox_Software/issues) |
| This manual or the website | [Open-BeatBox.github.io](https://github.com/Open-BeatBox/Open-BeatBox.github.io/issues) |
