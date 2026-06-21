from pathlib import Path

import pandas as pd

from backend.app.schemas import VehicleEstimateRequest, VehicleEstimateResponse


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "sample_vehicles.csv"


def load_vehicle_data() -> pd.DataFrame:
    """Load the sample vehicle dataset."""
    return pd.read_csv(DATASET_PATH)


def get_condition_adjustment(condition: str) -> int:
    """Return a price adjustment based on vehicle condition."""
    adjustments = {
        "Excellent": 2000,
        "Good": 0,
        "Average": -1500,
        "Poor": -3500,
    }

    return adjustments.get(condition, 0)


def estimate_vehicle_price(vehicle: VehicleEstimateRequest) -> VehicleEstimateResponse:
    """
    Estimate a used vehicle price using similar records from the sample dataset.

    This is still a baseline version, not the final machine-learning model.
    """

    data = load_vehicle_data()

    make = vehicle.make.lower()
    model = vehicle.model.lower()

    same_make_model = data[
        (data["make"].str.lower() == make)
        & (data["model"].str.lower() == model)
    ]

    same_make = data[data["make"].str.lower() == make]

    explanation = []

    if len(same_make_model) > 0:
        comparable_data = same_make_model
        confidence = "Medium"
        explanation.append(
            f"Found {len(comparable_data)} similar vehicles with the same make and model."
        )
    elif len(same_make) > 0:
        comparable_data = same_make
        confidence = "Low"
        explanation.append(
            f"No exact model match found, so the estimate used {len(comparable_data)} vehicles from the same make."
        )
    else:
        comparable_data = data
        confidence = "Low"
        explanation.append(
            "No matching make or model found, so the estimate used the overall sample dataset."
        )

    average_price = comparable_data["price"].mean()
    average_year = comparable_data["year"].mean()
    average_odometer = comparable_data["odometer"].mean()

    estimated_price = average_price

    # Year adjustment
    year_difference = vehicle.year - average_year
    year_adjustment = year_difference * 1000
    estimated_price += year_adjustment

    if year_adjustment > 0:
        explanation.append(
            f"Newer vehicle year increased the estimate by approximately ${int(year_adjustment)}."
        )
    elif year_adjustment < 0:
        explanation.append(
            f"Older vehicle year reduced the estimate by approximately ${abs(int(year_adjustment))}."
        )

    # Odometer adjustment
    odometer_difference = vehicle.odometer - average_odometer
    odometer_adjustment = -(odometer_difference / 10000) * 400
    estimated_price += odometer_adjustment

    if odometer_adjustment > 0:
        explanation.append(
            f"Lower odometer reading increased the estimate by approximately ${int(odometer_adjustment)}."
        )
    elif odometer_adjustment < 0:
        explanation.append(
            f"Higher odometer reading reduced the estimate by approximately ${abs(int(odometer_adjustment))}."
        )

    # Condition adjustment
    condition_adjustment = get_condition_adjustment(vehicle.condition)
    estimated_price += condition_adjustment

    if condition_adjustment > 0:
        explanation.append(
            f"{vehicle.condition} condition increased the estimate by approximately ${condition_adjustment}."
        )
    elif condition_adjustment < 0:
        explanation.append(
            f"{vehicle.condition} condition reduced the estimate by approximately ${abs(condition_adjustment)}."
        )
    else:
        explanation.append(f"{vehicle.condition} condition kept the estimate unchanged.")

    # Transmission adjustment
    if vehicle.transmission.lower() == "automatic":
        estimated_price += 500
        explanation.append("Automatic transmission slightly increased the estimate.")

    estimated_price = max(int(round(estimated_price, -2)), 2000)

    min_price = int(estimated_price * 0.9)
    max_price = int(estimated_price * 1.1)

    return VehicleEstimateResponse(
        estimated_price=estimated_price,
        min_price=min_price,
        max_price=max_price,
        confidence=confidence,
        explanation=explanation,
    )