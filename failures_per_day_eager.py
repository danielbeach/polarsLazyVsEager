import time
import polars as pl

start = time.perf_counter()

df = pl.read_csv('data_Q4_2025/*.csv')

failures_per_day = (
    df
    .filter(pl.col("failure") == 1)
    .group_by("date")
    .agg(pl.len().alias("failure_count"))
    .sort("date")
)

failures_per_day.write_csv("failures_per_day_eager.csv")

elapsed = time.perf_counter() - start
print(f"Done in {elapsed:.2f}s — written to failures_per_day_eager.csv")
