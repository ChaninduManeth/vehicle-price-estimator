from fastapi import FastAPI

from backend.app.estimator import estimate_vehicle_price
from backend.app.schemas import VehicleEstimateRequest, VehicleEstimateResponse

app = FastAPI(
    title="Vehicle Price Estimator API",
    description="Backend API for estimating used vehicle market values.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    """Return basic information about the API."""
    return {
        "message": "Vehicle Price Estimator API",
        "status": "running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """Confirm that the backend service is running."""
    return {
        "status": "healthy",
    }


@app.post("/estimate", response_model=VehicleEstimateResponse)
def estimate_price(vehicle: VehicleEstimateRequest) -> VehicleEstimateResponse:
    """Estimate the market value of a used vehicle."""
    return estimate_vehicle_price(vehicle)