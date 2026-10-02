# How it works

This page follows **one trial** from the animal's behaviour to the line in your data file. If you understand this page, every other page in the manual will make sense. No programming knowledge is needed.

## The chain in one picture

```text
   ┌──────────┐      ┌───────────────────────────────┐      ┌─────────────┐      ┌──────────┐
   │  Mouse   │◄────►│   Peripheral modules          │◄────►│ MAIN module │◄────►│  Your PC │
   │          │      │   feeder · screens · tunnel   │ CAN  │ (switch-    │serial│  control │
   │          │      │   lighting · nosepoke         │ bus  │  board)     │      │  app     │
   └──────────┘      └───────────────────────────────┘      └─────────────┘      └────┬─────┘
    behaviour          sensors and actuators, each             translates and          │
                       with its own small computer             forwards messages       ▼
                                                                                 CSV result files
```

There are only four ideas to hold on to:

1. **Every module is autonomous.** Each peripheral module (feeder, screen, tunnel…) has its own microcontroller. It reads its own sensors, handles its own timing, and *announces* what happened without being asked.
2. **Modules talk over a shared cable, the CAN bus.** CAN ("Controller Area Network") is the same kind of robust two-wire network used inside cars. Each message says who it is from or for, how urgent it is, and what it means. Details are in {doc}`software/firmware/can-intermodule-protocol`.
3. **The main module is a switchboard, not a brain.** It is the only module your PC talks to. It translates PC commands into CAN messages and CAN messages back into PC reports. It does **not** run the experiment.
4. **The PC runs the experiment.** The control application holds the protocol (the "training stage"), decides what to show and when to reward, and writes the log files.

## What happens in one trial

This is a trial of the screen-choice task (stages S2–S4, see {doc}`software/stages`). Names in **bold** are the modules from the table in {doc}`overview`.

```text
 1  PC     waits the inter-trial interval (a rest period you can configure)
 2  Mouse  enters the tunnel
 3  Tunnel module sees the infrared beams broken, in order, and reports "crossing"      ──► PC
 4  PC     picks a pattern for each screen according to the configuration
 5  PC     "show pattern A on the left, pattern B on the right"                         ──► Main ──► Screens
 6  Mouse  touches / pokes one of the screens
 7  Screen module reports the response                                                  ──► PC
 8  PC     compares it with the correct side
            ├─ correct   → turns the screens off, asks the feeder for a pellet
            └─ incorrect → flashes the screens, waits, then starts a corrective loop
 9  PC     switches the feeder's reward line on                                          ──► Main ──► Feeder
10  Feeder turns its disc; a pellet falls past its infrared sensor, which reports
        "pellet present"                                                                ──► PC
        (if no pellet is seen within about a second, the PC simply tries again)
11  PC     switches the reward line off. Mouse takes the pellet: the sensor clears      ──► PC
12  PC     records the trial, updates the success rate, and goes back to step 1
```

At every step the PC writes a line to the **event log**, and at the end of each trial one line to the **trial log** (see {doc}`software/data-output`).

```{admonition} Why does the application talk about "pins"?
:class: note
The previous generation of the box (**V2**) used an Arduino Mega as its main controller, and the application was written to switch electrical *pins* on and off and read other pins back. Rather than rewrite the application, the new main module **emulates** that old board: the application still sends and receives "pin words", and the main module turns each pin change into the right CAN message for the right module. This is why the application's configuration file still lists pin numbers, and why you will sometimes see the name "V2" in the firmware. New host protocols can be added later without touching the modules. See {doc}`software/firmware/architecture`.
```

## Who does what

| Question | Answer | Where it lives |
| --- | --- | --- |
| Which task is the mouse doing, and is it learning? | The **PC application** (training stage, success rate, stage change) | `pc_app/` in the Software repository ({doc}`project/repositories`) |
| Which module receives that command, and in what format? | The **main module firmware** (translation to CAN) | `micropython/modules/main_module/main_module.py` |
| How is a pellet actually delivered, and what if it jams? | The **feeder firmware** drives the motor and reports the sensor; the **PC application** decides when to retry | `micropython/modules/feeder.py`, `pc_app/…/experiment_managers/` |
| What does the screen draw, and when does it report a touch? | The **screen firmware** | `micropython/modules/screenmodule.py` |
| What are the circuit boards, and how are they powered? | The **hardware repository** (KiCad files) | the Hardware repository ({doc}`project/repositories`) |
| How do I build it? | The **assembly tutorials** | {doc}`build/index` |

## Timing you can rely on, and timing you cannot

- During experiments the **PC owns the reward timing**: it runs the feeder motor, watches the pellet sensor, and retries if no pellet appears. As a safety net, the feeder stops the motor by itself after 15 seconds if the "off" command never arrives.
- The feeder can also deliver a reward **on its own** when asked with a single request (this is what the `FEED` test command does): it turns a fraction of a turn, waits up to 0.5 s for the pellet, and repeats up to **20 times (about 10 seconds)** before reporting an error. The host must never assume a fixed delay.
- Events such as a screen response or a tunnel crossing are sent with a higher priority than status chatter, so they are not delayed by it.
- The MicroPython firmware can feel sluggish under heavy load (for example, many infrared events in a very short time). This is a known development item, tracked in {doc}`project/status`.

## Two ways to talk to the main module

| Mode | Used for | Who speaks |
| --- | --- | --- |
| **V2 emulation** (default) | Real experiments | The PC control application |
| **CLI mode** | First power-up, debugging, validating a module | You, typing short text commands such as `SCAN` or `FEED` ({doc}`software/firmware/cli`) |

The mode is chosen when the main module is flashed, and the two are never active at the same time.

## Next

- Want to build it? → {doc}`build/index`
- Want to run it? → {doc}`getting-started`
- Want the vocabulary? → {doc}`glossary`
