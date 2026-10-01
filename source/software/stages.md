# Training stages S1–S4

The application trains an animal in **stages**. Each stage is a small program (a *state machine*: a fixed sequence of phases) that decides what happens, what is rewarded, and when the animal has learned enough to move on. They build on one another: S2 extends S1, S3 extends S2, and so on.

```{admonition} Reading this page
:class: note
This page describes the logic **as implemented in the current development version** of the application. The parameter values quoted ("the example configuration") are the ones shipped in `experiment.cfg`; yours may differ. Protocol templates validated for publication are still being prepared ({doc}`../protocols/index`).
```

## The stages at a glance

| Stage | What the animal learns | A trial ends when… | The stage is complete when… |
| --- | --- | --- | --- |
| **S1** | The feeder gives pellets, and where to collect them | the pellet is collected | *n_trials* pellets have been collected |
| **S2** | Entering the tunnel, then **touching a screen**, brings a pellet | the pellet is collected after a correct touch | the success rate over the last *n_trials* responses reaches the **learning threshold** |
| **S3** | **Choosing the correct screen** (the one showing the rewarded pattern) | the pellet is collected after a correct touch | the success rate reaches the threshold **on both the left and the right side** |
| **S3.1** | As S3 but **without** the corrective loop | as S3 | as S3 |
| **S4** | As S3, plus a **third "discovery" pattern** rewarded only some of the time | as S3 | as S3 (with a stricter example threshold) |

## S1 — "food comes from the feeder"

No screens, no tunnel. The simplest stage, used to teach that the feeder delivers pellets and where they appear.

```text
INIT → ITI → DELIVER_PELLET → WAIT_PELLET ──pellet seen──► WAIT_PELLET_RETRIEVAL ──taken──► (next trial)
                 ▲                │ no pellet within 1 s                                        │
                 └────────────────┘ (try again)                         enough pellets? ─ yes → DONE
```

1. **ITI** — wait the inter-trial interval.
2. **DELIVER_PELLET** — run the feeder.
3. **WAIT_PELLET** — wait up to 1 s for the feeder sensor to see a pellet; if not, deliver again. A counter of retries drives the red pellet alert in the window.
4. **WAIT_PELLET_RETRIEVAL** — wait until the animal takes the pellet (the sensor clears). One more pellet is counted.
5. Repeat until *n_trials* pellets have been collected.

## S2 — "touch a screen to get a pellet"

The first stage with screens and the tunnel.

```text
ITI → WAIT_TUNNEL ─crossing─► SHOW_STIM → WAIT_TOUCH ─correct──► CORRECT_RESPONSE → DELIVER_PELLET → … → (next trial)
                                                │
                                                └incorrect─► INCORRECT_RESPONSE (flash) → STOP_FLASH (pause) → ITI  (corrective loop)
```

1. **ITI**, then **WAIT_TUNNEL**: the animal must walk through the tunnel (a crossing is detected by the photobeam gate).
2. **SHOW_STIM**: each screen shows its pattern for this trial.
3. **WAIT_TOUCH**: the animal responds on the left or the right screen.
4. If the response is on the **correct side**: the screens go off and a pellet is delivered. When the animal collects it **within the time-pressure limit**, the trial is *valid*; later than that, the trial is *invalid* and does not count as a success.
5. If the response is on the **incorrect side**: both screens **flash** for the blink duration, then wait for the **corrective-loop** pause, and the trial is presented again.

Which side is correct, and what each screen shows, is set in the configuration ({doc}`configuration`). With the example configuration, both screens show the *same* pattern (a grid) so that **every touch is correct**: S2 only teaches the animal to touch a screen.

**Success rate.** The application keeps the last *n_trials* responses for each side. A response counts as a success only if it is *valid* (correct side and pellet collected in time). The rate is successes divided by successes plus errors.

## S3 — "choose the correct screen"

S3 uses the S2 logic, with a different pair of patterns (in the example, horizontal lines are correct and vertical lines incorrect) so that the animal must **discriminate** between the screens. The difference from S2 is the completion rule:

> Both the **left** and the **right** side must have at least *n_trials* recorded responses, and **each** side's success rate must reach the learning threshold.

This stops an animal from passing the stage by always going to the same side. The window shows the left and right performance and the corrective-loop count.

## S3.1 — S3 without the corrective loop

Identical to S3 except that after an incorrect response there is **no corrective loop**: the screens flash, the trial is advanced, and a new trial starts after the usual rest.

## S4 — adding a discovery pattern

S4 inherits S3 and adds a **discovery pattern**: a third pattern (in the example, a diagonal) that is neither "correct" nor "incorrect". When the animal touches the screen showing it, a **random draw** decides whether it is rewarded:

- with probability **`reward_prob`** (0.5 in the example) the animal receives **`nb_rewards`** pellets (3 in the example);
- otherwise it receives nothing.

The panel counts discovery responses and rewards, and the discovery-versus-correct and discovery-versus-incorrect ratios are tracked. The stage ends with the same rule as S3 (both sides at the threshold), and the example threshold is stricter (0.95).

## Patterns shown on screens

The patterns available in configuration are white (`w`), black (`b`), vertical lines (`v`), horizontal lines (`h`), grid (`g`) and the two diagonals (`trbl`, `tlbr`). After a wrong response both screens **blink** between white and black.

## Moving between stages

If you choose **All** at start-up, the application starts S1 and moves to the next stage whenever one completes. After S4 it shows *Experiment complete*. Otherwise each stage runs on its own and stops when complete.

## Good to know

- **What counts as "nose_poke" in the application is the food-well sensor at the feeder.** The pin table inherited from the previous generation calls it that; the dedicated nosepoke module is not used by these stages.
- The **configuration** controls almost everything above: {doc}`configuration`.
- Every trial and every sensor change is recorded: {doc}`data-output`.
