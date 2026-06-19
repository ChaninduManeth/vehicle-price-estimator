from typing import Literal

from pydantic import BaseModel, Field


VehicleCondition = Literal["Excellent", "Good", "Average", "Poor"]


class VehicleEstimateRequest(BaseModel):
    make: str = Field(..., min_length=1, example="Toyota")
    model: str = Field(..., min_length=1, example="Corolla")
    year: int = Field(..., ge=1990, le=2026, example=2018)
    odometer: int = Field(..., ge=0, le=1000000, example=95000)
    condition: VehicleCondition = Field(..., example="Good")
    transmission: str = Field(..., example="Automatic")
    fuel_type: str = Field(..., example="Petrol")
    location: str = Field(..., example="VIC")


class VehicleEstimateResponse(BaseModel):
    estimated_price: int
    min_price: int
    max_price: int
    confidence: str
    explanation: list[str]