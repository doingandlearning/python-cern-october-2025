import json
import pandas as pd

with open("weather.json") as file:
    data = json.load(file)

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temp_c": data["hourly"]["temperature_2m"],
    "rh_pct": data["hourly"]["relativehumidity_2m"]
})

# Check the data
print(df.head())
print(df.tail())
print(df.sample(5))

df["time"] = pd.to_datetime(df["time"])

print(df.describe())

out = df.copy()
out["temp_c_roll3"] = out["temp_c"].rolling(window=3, min_periods=3).mean()

out.to_csv("weather.csv")

# hourly = out.resample("1H").mean(
out["hour"] = out.index
print(out.head())

g = out.groupby("hour").agg(temp_mean=("temp_c", "mean"), temp_std=("temp_c", "std"), rh_mean=("rh_pct", "mean"))

