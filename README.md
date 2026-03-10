# testpolars

Exploratory scripts for learning [Polars](https://pola.rs/) — a fast DataFrame library for Python. Covers eager vs. lazy (streaming) evaluation using real-world datasets.

## Datasets

**Backblaze Hard Drive Stats (Q4 2025)** — `data_Q4_2025/`
Daily CSVs of hard drive SMART telemetry from Backblaze datacenters, with a `failure` column indicating drive failures.

**Divvy Bike Share** — `*-divvy-tripdata.csv`
Monthly trip data from Chicago's Divvy bikeshare system, with `started_at` timestamps per ride.

## Scripts

| Script | Dataset | Mode | Output |
|---|---|---|---|
| `rides_per_day.py` | Divvy trip CSVs | Lazy / streaming | `rides_per_day.csv` |
| `failures_per_day_eager.py` | Backblaze Q4 2025 | Eager | `failures_per_day_eager.csv` |
| `failures_per_day_lazy.py` | Backblaze Q4 2025 | Lazy / streaming | `failures_per_day_lazy.csv` |

### rides_per_day.py
Scans all Divvy trip CSVs with `scan_csv` (lazy + streaming), parses the `started_at` datetime column into a date, groups by date, and counts rides per day.

### failures_per_day_eager.py
Reads all Q4 2025 Backblaze CSVs into memory with `read_csv` (eager), filters for rows where `failure == 1`, and counts failures per day.

### failures_per_day_lazy.py
Same query as the eager version but uses `scan_csv` + `sink_csv` with streaming engine — useful for comparing performance and memory usage against the eager approach.

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Running

```bash
uv run rides_per_day.py
uv run failures_per_day_eager.py
uv run failures_per_day_lazy.py
```

Each script prints elapsed time and the output CSV path when done.
