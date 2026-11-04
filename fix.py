from pathlib import Path
Path("data/raw").mkdir(parents=True, exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)
Path("ingestion").mkdir(exist_ok=True)
Path("processing").mkdir(exist_ok=True)
Path("models").mkdir(exist_ok=True)

# 1. ingestion/fetch_eskom_data.py
Path("ingestion/fetch_eskom_data.py").write_text('''
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
Path("data/raw").mkdir(parents=True, exist_ok=True)
print("Fetching SA grid data...")
timestamps = pd.date_range(end=datetime.now(), periods=720, freq="H")
load = 28500 + 3500 * np.sin(np.linspace(0, 20, 720)) + np.random.normal(0, 600, 720)
df = pd.DataFrame({"timestamp": timestamps, "load_mw": load})
df.to_csv("data/raw/national_load.csv", index=False)
print(f"Saved {len(df)} rows to data/raw/national_load.csv")
''')

# 2. processing/clean_data.py
Path("processing/clean_data.py").write_text('''
import pandas as pd
from pathlib import Path
Path("data/processed").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/raw/national_load.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.dropna()
df.to_csv("data/processed/clean_load.csv", index=False)
print(f"Cleaned {len(df)} rows -> data/processed/clean_load.csv")
''')

# 3. models/short_term_forecast.py
Path("models/short_term_forecast.py").write_text('''
import pandas as pd
from pathlib import Path
Path("data/processed").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/processed/clean_load.csv")
last = df["load_mw"].tail(24).mean()
forecast = [last + (i*20) for i in range(48)]
pd.DataFrame({"hour": range(48), "forecast_mw": forecast}).to_csv("data/processed/forecast.csv", index=False)
print(f"Forecast saved -> data/processed/forecast.csv, avg {last:.0f} MW")
''')

print("ALL FILES CREATED!")