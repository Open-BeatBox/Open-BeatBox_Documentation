# Status and open points

Open-BEATBox is a working platform, but not every part is finished. This page is the honest list: what is solid, and what is still open. It is meant for builders (so you know what to expect) and for contributors (so you know where help is needed).

## What is working

| Area | State |
| --- | --- |
| **Hardware V3** | Complete set of CAD files and eight KiCad board designs with manufacturing files; real boxes have been built |
| **Assembly tutorials** | Six module tutorials with videos, plus a Master BOM — marked `0.1-draft` |
| **Module firmware** | MicroPython programs for the main, feeder, nosepoke, screen, lighting and tunnel roles; CAN protocol; validation CLI |
| **PC application** | Qt interface with the five training stages S1–S4, CSV result files, multi-box control |
| **Manual** | This manual, built and published with the website |

## Open points

### Build and hardware

| # | Point | Effect on you |
| --- | --- | --- |
| H1 | The **Master BOM** has no rows for the main-module board (`BB_RPI_shield_V1`) or the nosepoke board, and no tutorial builds the main module | Use {doc}`../hardware/pcbs` and {doc}`../hardware/modules` for those |
| H2 | The BOM's source-file column still contains paths from the earlier layout (for example `02_CAD_files/V3/feeder_V3/…`), and some fields are marked with questions or placeholders | Do not treat unresolved rows as purchasing-ready; use {doc}`../hardware/mechanical` to locate files |
| H3 | Assembly documents have no hardware revision or verification date yet | Treat as draft; report discrepancies |
| H4 | Open validation items: final cost benchmark, optimal cable lengths, wall colour for tracking, long-term reliability | Figures on the website are provisional |
| H5 | The relationship between the main-module board and a single-board computer, and the physical link to the PC (USB per the Hardware README; UART0 through a USB-serial adapter per the Software README) need to be described precisely by the designers | Follow the Software README for wiring today |
| H6 | The mapping *tunnel = `IR_BARRIER` module* and *the stages use the feeder sensor, not the nosepoke module* is deduced from the firmware | Please confirm or correct |

### Firmware and protocol

| # | Point | Effect on you |
| --- | --- | --- |
| F1 | The **Firmware repository** is a placeholder that points to the Software repository, where the firmware lives (`micropython/`); it has no release of its own | See {doc}`../software/firmware/index` |
| F2 | The project carries **local modifications** to two third-party libraries, so they cannot simply point to their upstream projects. The plan agreed with the developers: copy them as plain folders ("flatten" them) into `micropython/libs/`, then publish them as forks and bring them back as Git submodules. `microPython_MCP2515` (CAN driver; upstream `capella-ben/microPython_MCP2515`, MIT licence, plus six project commits) is now copied this way. `CircuitPython_PCA9955B` (LED driver, used by the lighting module only; upstream `noelanderson/CircuitPython_PCA9955B`, MIT licence) is copied the same way, from the project's MicroPython port (branch `dev_mpy`, commit `f73fbfe`, July 2026), so `deploy_module.py lighting` works on a fresh clone. `beatbox-protocol` and the ILI9341 screen driver are Git submodules, fetched with `--recurse-submodules`. The fork URLs are still to be recorded | Nothing to do for now; see {doc}`../software/firmware/deploy` |
| F3 | The **left/right screen identity** is a one-line edit in `screenmodule.py` (it ships as the right screen) | Follow {doc}`../hardware/flashing-cards` |
| F4 | **Pattern numbering**: the pattern codes the application sends (4-bit V2 codes) and the numbers the screen program accepts (0–7) do not appear to be translated into each other | Verify each pattern on a real screen |
| F5 | The **CAN specification still differs from the code** for the IR barrier payloads, and does not enumerate the lighting group byte or the screen pattern numbers. The feeder section was corrected on 6 October 2026 and now matches the code. The developers confirmed that **the firmware is the reference** | Follow the code, as listed in section 8 of {doc}`../software/firmware/can-intermodule-protocol` |
| F6 | Roadmap: the handshake sometimes fails, the main module can drop CAN messages under load, MicroPython can feel laggy with many events, no on-board log storage, repository structure and naming need cleaning | Restart and retry; keep event rates reasonable |
| F7 | **Tests:** the firmware host tests (`micropython/tests/`) all pass since the developers' update of 6 October 2026 (`test_bb_comm_protocol.py` removed, feeder, IR-barrier and serial-manager tests rewritten). In `pc_app/tests/`, three files (`test_boot_fakes.py`, `test_serial_com.py`, `test_serial_com_threaded.py`) use a pseudo-terminal and run on Linux and macOS only | Run the tests on Linux or macOS for the full suite |
| F8 | On the ICM GitLab, the `beatbox-protocol` submodule URL still uses `git://`, whereas the GitHub repository uses `https://`. That library is public, so `https://` works for everyone without an account or key; a request to change the GitLab URL has been sent | None on GitHub clones, which use `https://` |

### PC application

| # | Point | Effect on you |
| --- | --- | --- |
| S1 | The settings file is read from inside the application folder, so use an **editable install** | {doc}`../software/install` |
| S2 | `--n-trials` and `--inter-trial-interval` are accepted but the window shows the file's values | Edit the file |
| S3 | Each stage section of `experiment.cfg` must repeat all parameters (no inheritance) | {doc}`../software/configuration` |
| S4 | The validator accepts the pattern letter `d`, but no pattern exists for it | Do not use `d` |
| S5 | In *advanced* mode, no check ensures that one screen shows the correct pattern on each trial | Design sequences carefully |
| S6 | Sensor and pin names (`nose_poke`, "V2") are inherited from the previous generation | Names will change |
| S7 | Graph plotting is not implemented yet | Analyse the CSV files |
| S8 | A refactor of the PC application (hardware-neutral names, entry point `beatbox.gui.app`) is in progress on the ICM GitLab branch `pc_app-dev` and is not in this release | None; the commands in this manual match the release |

### Documentation

| # | Point |
| --- | --- |
| D1 | The installation and deployment instructions were written from the repository files and **have not yet been run end-to-end on a clean machine** — feedback is welcome |
| D2 | The interface screenshots in the manual were taken with a **simulated box**; screenshots from a real session would be better (the older images in the repository show the previous-generation software) |
| D3 | Flashing and software walk-through videos are not yet available; captions or transcripts for the assembly videos are pending |
| D4 | Protocol templates and validation datasets are not yet published ({doc}`../protocols/index`) |
| D5 | The release `biorxiv-v1` was published on 9 November 2026 on the Hardware, Software and Documentation repositories and archived on Zenodo (Hardware [10.5281/zenodo.24080048](https://doi.org/10.5281/zenodo.24080048), Software [10.5281/zenodo.24080479](https://doi.org/10.5281/zenodo.24080479), Documentation [10.5281/zenodo.24080481](https://doi.org/10.5281/zenodo.24080481)); it accompanies the bioRxiv preprint. The preprint is posted on bioRxiv ([10.64898/2026.11.07.765109](https://doi.org/10.64898/2026.11.07.765109)); its DOI is in the READMEs, the `CITATION.cff` files and this manual ({doc}`repositories`). |
| D6 | The **MATLAB/Arduino implementation**, the **analysis code** and the **behavioural dataset** behind the preprint's results are not yet public. They are to be released with a licence and a Zenodo DOI before preprint v2 |

## How to help

Everything above can be tackled by contributors: testing the instructions on your machine, confirming the points marked *please confirm*, improving the BOM, adding screenshots, or sending a fix. See {doc}`../contributing`.
