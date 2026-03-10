import time
import polars as pl

pl.Config.set_engine_affinity("streaming")

start = time.perf_counter()

df = pl.scan_csv('*-divvy-tripdata.csv')

rides_per_day = (
    df.with_columns(pl.col("started_at").str.to_datetime().dt.date().alias("date"))
    .group_by("date")
    .agg(pl.len().alias("ride_count"))
    .sort("date")
)

rides_per_day.sink_csv("rides_per_day.csv")

elapsed = time.perf_counter() - start
print(f"Done in {elapsed:.2f}s — written to rides_per_day.csv")
