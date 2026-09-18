# Data & Analysis

How to capture, store, and analyze data from Open-BEATBox cages while keeping sessions reproducible and auditable.

## Data pipeline (conceptual)
1. **Acquisition**: firmware/runtime emits structured events (sensor triggers, actuator states, timestamps, task variables).
2. **Transport**: logs saved locally (filesystem) and/or streamed to a collector (HTTP, MQTT, or WebSocket) over USB or Wi‑Fi.
3. **Storage**: append-only raw logs; optional database or object storage for aggregation.
4. **Processing**: convert raw logs to analysis-ready tables, merge with metadata (subject, task version, cohort).
5. **Visualization/analysis**: notebooks or dashboards for QC, performance, and longitudinal trends.

## Logging guidelines
- Use structured formats (JSON lines or CSV) with explicit field names and units.
- Include: timestamp (ISO 8601, with timezone or UTC), device ID, subject ID, task version, firmware/runtime version, and configuration hash.
- Record both sensor events and actuator commands; mark errors and retries.
- Keep a manifest per session linking raw logs to metadata (subject, cohort, task parameters).
- When available, export JSON-LD metadata to align with FAIR workflows.

## Sync and retention
- Offload logs after each session or daily; avoid long-running local-only storage.
- Verify transfers (hashes/checksums) before deleting local copies.
- Define retention policies for raw vs. processed data; keep raw indefinitely when feasible.
- Python client and REST/WebSocket APIs can stream data to your collector; include device and session identifiers in streams.

## QC and monitoring
- Build a lightweight QC report per session: event counts, latency distributions, reward totals, and missing data flags.
- Track device health: uptime, dropped packets, storage utilization, temperature.
- Alert on clock drift, missing heartbeats, or failed log uploads.

## Analysis starter workflow
```bash
# Example sketch using Python/pandas for JSONL logs
python - <<'PY'
import json, pandas as pd, pathlib, glob

paths = glob.glob("data/raw/*.jsonl")
df = pd.concat(pd.read_json(p, lines=True) for p in paths)
df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

# Filter a session
session = df[df["session_id"] == "YOUR_SESSION_ID"].copy()

# Basic QC
print(session["event_type"].value_counts())
print(session.groupby("event_type")["latency_ms"].describe())
PY
```

## Reproducibility
- Version control task configs and firmware/runtime; include commit hashes in logs.
- Keep environment files for analysis (e.g., `requirements.txt` or `environment.yml`).
- Document preprocessing steps and notebook links per study.

## Data access control
- Anonymize subject IDs when sharing outside the core team.
- Avoid logging PII; limit metadata to study-relevant identifiers.
- For collaborative datasets, publish a data dictionary describing every field.
