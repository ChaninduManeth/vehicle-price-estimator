from fastapi import FastAPI

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