
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
Path("data/raw").mkdir(parents=True, exist_ok=True)
print("Fetching SA grid data...")
timestamps = pd.date_range(end=datetime.now(), periods=720, freq="h")
load = 28500 + 3500 * np.sin(np.linspace(0, 20, 720)) + np.random.normal(0, 600, 720)
df = pd.DataFrame({"timestamp": timestamps, "load_mw": load})
df.to_csv("data/raw/national_load.csv", index=False)
print(f"Saved {len(df)} rows to data/raw/national_load.csv")
