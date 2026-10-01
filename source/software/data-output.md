# Data output

Every session writes **two CSV files** into the experiment folder you chose. CSV files are plain-text tables that open in Excel, LibreOffice, R, Python (pandas) or any text editor.

| File | One row per… | Use it for |
| --- | --- | --- |
| **Trial log** | trial (a response and its outcome) | Learning curves, success rates, response times |
| **Event log** | event (a sensor change or a message) | Detailed reconstruction of what happened; activity patterns |

## File names

```text
FULL_<animal>_S<stage>_<timestamp>.csv      ← event log
<animal>_S<stage>_<timestamp>.csv           ← trial log
```

- `<animal>` is the *Animal name* you typed at start-up (left out if empty).
- `S<stage>` is the stage number: `S1`, `S2`, `S3`, `S3.1`, `S4`.
- `<timestamp>` is the date and time the file was created, ISO format, with `:` replaced by `-` so it is a valid file name (for example `2026-10-01T14-05-33.123456`).

Example: `FULL_M012_S2_2026-10-01T14-05-33.123456.csv` and `M012_S2_2026-10-01T14-05-33.123456.csv`.

## Trial log

One row at the end of each trial, from stage S2 on (S1 does not fill this file).

| Column | Meaning |
| --- | --- |
| `date` | Date and time (ISO) when the rest period after the trial started |
| `show_stim_ts` | Time the stimulus was shown, in **seconds since the log was created** (`NA` if not applicable) |
| `screen_touch_ts` | Time of the screen response, same unit |
| `reward_collect_ts` | Time the pellet was collected, same unit |
| `total_trials` | Trials so far |
| `correct_side` | The correct side for this trial: `l`, `r` (or `x` if none, see {doc}`configuration`) |
| `response` | The side the animal responded on |
| `reward` | Whether a reward was given |
| `correct` | Correct response |
| `incorrect` | Incorrect response |
| `valid` | Correct response **and** pellet collected within the time-pressure limit |
| `corrective_loop` | Corrective-loop count |
| `overall_perf` | Success rate over the window, both sides |
| `perf_left`, `perf_right` | Success rate for each side |

The *reaction time* of a trial is `screen_touch_ts − show_stim_ts`; the *collection time* is `reward_collect_ts − screen_touch_ts`.

## Event log

One row **every time something changes or is logged**: a sensor edge, a phase change, an information or warning message.

| Column | Meaning |
| --- | --- |
| `date` | Absolute date and time (ISO), from the PC clock |
| `timestamp_s` | Seconds since the log was created |
| `stage` | Stage number |
| `log_level` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `message` | Human-readable text, for example "Correct response on left_response." |
| `correct_side` | Correct side of the current trial |
| `total_trials`, `trial_number` | Trial counters |
| `corrective_loop` | Corrective-loop count |
| `left_performance`, `right_performance` | Success rates at this moment |
| `state_<sensor>` | One column per sensor: `state_nose_poke`, `state_left_response`, `state_right_response`, `state_left_tunnel_crossing`, `state_right_tunnel_crossing`, `state_feed_alert`. The value is the level of that sensor at this moment. |

At the start of a stage the event log also holds the **animal's details** and the **settings used** ({doc}`configuration`), written as `INFO` messages. This makes each file self-describing.

```{admonition} Sensor names
:class: note
The sensor named `nose_poke` is the **pellet sensor at the feeder**; the name is inherited from the previous generation of the system. See {doc}`stages`.
```

## Opening and analysing

**Excel / LibreOffice:** double-click the file, or *Data → From text/CSV*. Use a period as the decimal separator.

**Python:**

```python
import pandas as pd

trials = pd.read_csv("M012_S2_2026-10-01T14-05-33.123456.csv")
trials["reaction_s"] = trials["screen_touch_ts"] - trials["show_stim_ts"]
print(trials[["total_trials", "valid", "overall_perf"]].tail())
```

**R:**

```r
trials <- read.csv("M012_S2_2026-10-01T14-05-33.123456.csv", na.strings = "NA")
```

## Good practice

- **Never edit the original files.** Work on copies.
- Copy the files off the experiment computer after each session and keep them with your configuration file and software version.
- Keep consistent animal names: they are the only link between a file and an animal.
- Use the `date` column for absolute time. The relative time columns restart for each stage.
- There is no automatic upload or database: data are files in a folder.
- The format may change while the software is in development; note the software version with the data.
