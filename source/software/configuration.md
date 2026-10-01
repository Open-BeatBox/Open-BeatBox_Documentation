# Configuring experiments

The experiment is controlled by one plain-text file, **`experiment.cfg`**, that you can open with any text editor. This page explains every setting.

## Where is the file?

In the Software repository: `pc_app/beatbox/config/experiment.cfg`. The application reads it when a stage starts. Because the application was installed in *editable* mode ({doc}`install`), this is the file you edit. **Close and restart the stage** (or the application) after editing.

```{admonition} Back up and record
:class: tip
Keep a copy of the exact `experiment.cfg` used for each cohort, next to the data. The application also writes the stage's settings into the event log at the start of each stage, so the values used are traceable.
```

The application **checks the file** against a specification (`config_specs/*.config.spec`). If a value is out of range or of the wrong type, the stage refuses to start and tells you which setting is wrong.

## File layout

```ini
# Global settings
n_trials = 4
inter_trial_interval = 2000

[S2]
n_trials = 4
inter_trial_interval = 2000
corrective_loop_timeout = 2000
error_flash_ms = 2000
learning_threshold = 0.55
correct_pattern = 'g'
incorrect_pattern = 'g'
screen_sequence = ['l', 'r', 'l', 'l', 'r', 'r']
time_pressure_ms = 15000
advanced = False
left_screen_sequence = ['v', 'w', 'v']
right_screen_sequence = ['h', 'v', 'b']

[S3]
# same parameters as [S2], with S3 values

[S3.1]
# same parameters as [S2], with S3.1 values

[S4]
# same parameters as [S2], plus discovery_pattern, reward_prob, nb_rewards
```

- Values at the top (outside any `[section]`) are used by **S1**.
- Each of `[S2]`, `[S3]`, `[S3.1]` and `[S4]` holds the settings of one stage.
- **Every section must list all parameters** of its stage, even those that do not change from S2: a section does not inherit from another. (This is a known inconvenience.)
- Text values are in quotes (`'h'`), lists in square brackets (`['l', 'r']`), numbers without quotes. Lines starting with `#` are comments.

## Parameters

| Parameter | Unit | Used by | Meaning |
| --- | --- | --- | --- |
| `n_trials` | count | all | **S1:** number of pellets to collect. **S2+:** the size of the *sliding window* of last responses (per side) used to compute the success rate. |
| `inter_trial_interval` | ms | all | Rest between two trials. |
| `learning_threshold` | 0–1 | S2+ | Success rate the animal must reach to complete the stage (0.8 = 80 %). |
| `corrective_loop_timeout` | ms | S2+ | Pause after an error flash before the same trial is shown again. |
| `error_flash_ms` | ms | S2+ | How long both screens blink after an incorrect response. |
| `time_pressure_ms` | ms | S2+ | Maximum time between a correct response and collecting the pellet; slower collection makes the trial *invalid*. |
| `correct_pattern` | pattern | S2+ | The pattern that marks the **correct** screen. |
| `incorrect_pattern` | pattern | S2+ | The pattern shown on the **incorrect** screen. Same as `correct_pattern` ⇒ every touch is correct. |
| `screen_sequence` | list of `'l'`/`'r'` | S2+ | Which screen is correct on each trial, cycled in order. Used when `advanced = False`. |
| `advanced` | True/False | S2+ | `False`: use `screen_sequence` with `correct_pattern`/`incorrect_pattern`. `True`: use the two explicit sequences below. |
| `left_screen_sequence`, `right_screen_sequence` | list of patterns | S2+ (when `advanced = True`) | The pattern shown on each screen on each trial, cycled in order. |
| `discovery_pattern` | pattern | S4 | The third pattern whose reward is probabilistic. |
| `reward_prob` | 0–1 | S4 | Probability that touching the discovery pattern is rewarded. |
| `nb_rewards` | count | S4 | Number of pellets given when the draw succeeds. |

### Patterns

| Letter | Pattern |
| --- | --- |
| `w` | Full white |
| `b` | Full black |
| `v` | Vertical lines |
| `h` | Horizontal lines |
| `g` | Grid |
| `trbl` | Diagonal lines, top-right to bottom-left |
| `tlbr` | Diagonal lines, top-left to bottom-right |

```{admonition} Advanced mode: keep the sequences complementary
:class: warning
In *advanced* mode the application finds the correct side as the one showing `correct_pattern`. **No check ensures that at least one screen shows it on every trial**: if neither does, the trial has no correct side and an error is logged. Design the two sequences so that, on every position, exactly one screen shows the correct pattern. (In S4, a third pattern, `discovery_pattern`, is allowed in place of the incorrect one.)
```

The specification also accepts the letter `d` in sequences, but the application has no pattern for it: do not use it.

### Cycling

The lists are read **in a loop**: trial 1 uses the first item, trial 2 the second, and so on, starting again at the beginning when the end is reached. Lists of different lengths are allowed in advanced mode.

## Examples

### S3: horizontal lines are rewarded, vertical lines are not

```ini
[S3]
n_trials = 10
inter_trial_interval = 2000
corrective_loop_timeout = 1000
error_flash_ms = 2000
learning_threshold = 0.6
correct_pattern = 'h'
incorrect_pattern = 'v'
screen_sequence = ['l', 'r', 'l', 'l', 'r', 'r']
time_pressure_ms = 15000
advanced = False
left_screen_sequence = ['h', 'h', 'w', 'b', 'v', 'h', 'h']
right_screen_sequence = ['b', 'v', 'h', 'h', 'h', 'v', 'h']
```

The correct screen is **left, right, left, left, right, right**, and the sequence repeats.

### S4: the discovery pattern

```ini
[S4]
# (other parameters as in [S3])
advanced = True
correct_pattern = 'h'
incorrect_pattern = 'v'
discovery_pattern = 'trbl'
reward_prob = 0.5
nb_rewards = 3
left_screen_sequence = ['h', 'trbl', 'trbl', 'h', 'h', 'b', 'h']
right_screen_sequence = ['trbl', 'h', 'b', 'b', 'v', 'trbl', 'h']
```

## Other configuration files

| File | Purpose |
| --- | --- |
| `pc_app/beatbox/config/pins_config.cfg` | Names and numbers of the sensors and actuators (inherited from the previous-generation controller). **You should not have to change it**, and its defaults must match the firmware. |
| `pc_app/mock_experiment/experiment.cfg` | Example for the `--from-config-file` start-up option |

## Good practice

- Change **one thing at a time** between cohorts and note it.
- Use a short, safe configuration (small `n_trials`, short intervals) for a dry run before an animal goes in, and restore the real values afterwards.
- Do not change the file while a stage is running.
