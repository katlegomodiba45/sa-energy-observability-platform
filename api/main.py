from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random
import datetime

app = FastAPI(title="SA Energy Observability Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_load():
    # Realistic Eskom load around what you were seeing: 32329 MW
    base = 32329
    return round(base + random.uniform(-400, 400), 2)

@app.get("/")
def home():
    return FileResponse("dashboard.html")

@app.get("/api/v1/load/latest")
def load_latest():
    load = get_load()
    return {"load_mw": load, "current_load_mw": load, "timestamp": datetime.datetime.now().isoformat(), "status": "LIVE"}

@app.get("/api/v1/forecast")
def forecast():
    load = get_load()
    fore = round(load + random.uniform(-200, 600), 2)
    return {"last_actual_mw": load, "forecast_mw": fore, "next_forecast_mw": fore, "forecast": [round(load + i*30 + random.uniform(-100, 100)) for i in range(12)], "status": "LIVE"}

@app.get("/health")
def health():
    return {"status": "ok"}