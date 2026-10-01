# Getting started

This page is the map from "I have nothing" to "my first experiment is running". Find your starting point, then follow the numbered path. Each step links to the page that explains it in detail.

## Pick your starting point

| You are… | Start at |
| --- | --- |
| **Evaluating** the project | {doc}`overview` and {doc}`how-it-works` |
| **A builder** with no box yet | Step 1 below |
| **An experimenter** whose lab already has a box | Step 7 below |
| **A developer** who wants to change the code | {doc}`software/development` |

## The full path

```text
 1 Check the plan ─► 2 Order & make parts ─► 3 Flash the boards ─► 4 Assemble modules
                                                                          │
 8 Run your experiment ◄─ 7 Install the PC app ◄─ 6 Test with the CLI ◄─ 5 Integrate & power up
```

### 1. Check the plan

- Read the {doc}`build/safety` notes (inserts, soldering, plexiglass).
- Be aware that **soldering is required** for the screen and infrared-sensor assemblies. If you have no soldering equipment, plan for help.
- Download the {doc}`Master BOM <build/bom>` and confirm the hardware revision you intend to build. The manual targets **V3**.

### 2. Order and make the parts

- **Circuit boards:** upload the manufacturing files from the Hardware repository to a PCB service; assembled boards are recommended. See {doc}`hardware/ordering-pcbs`.
- **Purchased components:** motor, screens, connectors, cables, power supply, camera — listed in the BOM and in {doc}`hardware/pcbs`.
- **Plastic and acrylic parts:** 3D-print and laser-cut from the files in the Hardware repository. See {doc}`build/fabrication` and {doc}`hardware/mechanical`.

```{admonition} Git LFS
:class: tip
The large `.STEP` and `.zip` files in the Hardware repository are stored with Git LFS. If you clone the repository, run `git lfs install` first, or download the files from the GitHub web page instead.
```

### 3. Flash the module boards

Each module board must receive its firmware **before** it is closed inside its housing. This needs a USB cable and a computer, but not a programmer's knowledge. Follow {doc}`hardware/flashing-cards`.

### 4. Assemble the modules

Follow the six tutorials in order (frame, bottle mount, feeder, light ring, photobeam gate, screens). They are listed in {doc}`build/assembly` and have a video each ({doc}`build/video-tutorials`).

### 5. Integrate and power up

Install the modules in the enclosure, connect the cables, and power the system from the 12 V supply. Then run the checks in {doc}`build/first-power-up`.

### 6. Test with the command-line tool

Before using the full application, confirm that every module answers using the validation tool: type `SCAN` and watch the modules report in. See {doc}`software/firmware/cli`.

### 7. Install the PC application

Install Python (via conda), the application and its dependencies, then start the application. See {doc}`software/install`.

### 8. Run your experiment

Choose a stage, enter the animal's details, press start. The stages build on each other from "learn that food comes from the feeder" to "choose the correct screen":

| Stage | In one sentence |
| --- | --- |
| **S1** | The animal learns that the feeder delivers pellets and how to collect them. |
| **S2** | The animal enters the tunnel, then touches a screen to earn a pellet. |
| **S3** | The animal must choose the screen showing the correct pattern; a wrong choice triggers a corrective loop. |
| **S3.1** | As S3, but without the corrective loop. |
| **S4** | A third "discovery" pattern is added that is rewarded only part of the time. |

Details: {doc}`software/stages`. Where the data goes: {doc}`software/data-output`.

## Before putting an animal in

Always check, with **no animal present**:

- [ ] Every module appears in `SCAN` and reports `IDLE`.
- [ ] A test reward (`FEED`) delivers a pellet, and the feeder sensor sees it.
- [ ] Both screens show the test pattern and respond to a touch / poke.
- [ ] The lighting module switches white, red and infrared.
- [ ] Every cable is secured out of reach of the animal, and there are no sharp edges.
- [ ] You have done a short dry run of stage S1 and found the log files.

Your local animal-welfare and ethical approvals apply to any use with animals. Open-BEATBox is a research tool, not a certified product.

## Stuck?

- {doc}`troubleshooting`
- {doc}`glossary`
- [GitHub Discussions](https://github.com/Open-BeatBox/Open-BeatBox.github.io/discussions) for questions and sharing builds.
