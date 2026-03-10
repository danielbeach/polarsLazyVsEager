import time
import polars as pl

pl.Config.set_engine_affinity("streaming")

start = time.perf_counter()

df = pl.scan_csv('data_Q4_2025/*.csv')

failures_per_day = (
    df
    .filter(pl.col("failure") == 1)
    .group_by("date")
    .agg(pl.len().alias("failure_count"))
    .sort("date")
)

failures_per_day.sink_csv("failures_per_day_lazy.csv")

elapsed = time.perf_counter() - start
print(f"Done in {elapsed:.2f}s — written to failures_per_day_lazy.csv")
