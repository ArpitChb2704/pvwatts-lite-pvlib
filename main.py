from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from solar_engine import run_simulation

app = FastAPI()


class SolarInput(BaseModel):
    lat: float = Field(..., ge=-90, le=90, description="Latitude (-90 to 90)")
    lon: float = Field(..., ge=-180, le=180, description="Longitude (-180 to 180)")
    
    system_size_kw: float = Field(4, gt=0, description="System size in kW")
    tilt: float = Field(25, ge=0, le=90, description="Tilt angle")
    azimuth: float = Field(180, ge=0, le=360, description="Azimuth angle")

    shading_factor: float = Field(0.95, ge=0, le=1, description="0 to 1")

    losses: List[float] = Field(
        default=[2, 3, 2, 1],
        description="List of loss percentages"
    )


@app.post("/predict")
def predict(data: SolarInput):
    result = run_simulation(
        lat=data.lat,
        lon=data.lon,
        system_size_kw=data.system_size_kw,
        tilt=data.tilt,
        azimuth=data.azimuth,
        losses=data.losses,
        shading_factor=data.shading_factor
    )
    return result