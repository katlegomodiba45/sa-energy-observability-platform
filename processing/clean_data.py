
import pandas as pd
from pathlib import Path
Path("data/processed").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/raw/national_load.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.dropna()
df.to_csv("data/processed/clean_load.csv", index=False)
print(f"Cleaned {len(df)} rows -> data/processed/clean_load.csv")
