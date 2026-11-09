# Protocols

This section is about the **behavioural protocols**: the tasks an animal performs in the box. (Not to be confused with the *communication* protocols between modules, which are in {doc}`../software/firmware/can-intermodule-protocol`.)

## Intended use cases

- Autonomous operant conditioning.
- Reward-delivery tasks.
- Sensor-triggered behavioural events.
- Longitudinal home-cage monitoring.
- Circadian and motivational dynamics.

## Protocols implemented today

The control application ships a training sequence of five stages: S1, S2, S3, S3.1 and S4. They are described in {doc}`../software/stages` and parameterised in {doc}`../software/configuration`.

| Stage | Task | Typical aim |
| --- | --- | --- |
| S1 | Collect pellets from the feeder | Habituation to the feeder |
| S2 | Cross the tunnel, touch a screen for a pellet | Learn the action–outcome link |
| S3 | Choose the screen showing the rewarded pattern (with corrective loop) | Visual discrimination |
| S3.1 | As S3, without the corrective loop | Discrimination without correction |
| S4 | As S3 plus a probabilistic "discovery" pattern | Exploration and reward-probability sensitivity |

A full set of parameters for each stage is in the example configuration. These are **working examples, not validated protocol templates**.

## Building your own protocol

The modular design makes it possible to define other tasks:

- **Change the existing stages** by editing the parameters: patterns, sequences, thresholds, timing, reward probability.
- **Add a stage** in the PC application by extending a state machine ({doc}`../software/development`).
- **Add a module** with its own firmware and CAN messages ({doc}`../software/firmware/can-intermodule-protocol`).
- **Combine with other tools.** The box is designed to work alongside camera-based monitoring or other open-source acquisition tools; the box itself does not provide video (see {doc}`../hardware/modules`).

## Validation status

The platform is nearing deployment through real builds, assembly documentation and beta-unit preparation. Quantitative benchmarks, final protocol templates and validation datasets are **not yet published**; they will be added here as they become available.

When you publish results obtained with Open-BEATBox, report: the **hardware revision**, the **software and firmware versions**, the **stage**, and the **configuration file** you used.

## Citing

Cite the reference preprint and the Zenodo record of the release you used; both are listed in {doc}`../project/repositories`. Each repository also carries a `CITATION.cff` file.
