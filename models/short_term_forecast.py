
import pandas as pd
from pathlib import Path
Path("data/processed").mkdir(parents=True, exist_ok=True)
df = pd.read_csv("data/processed/clean_load.csv")
last = df["load_mw"].tail(24).mean()
forecast = [last + (i*20) for i in range(48)]
pd.DataFrame({"hour": range(48), "forecast_mw": forecast}).to_csv("data/processed/forecast.csv", index=False)
print(f"Forecast saved -> data/processed/forecast.csv, avg {last:.0f} MW")
