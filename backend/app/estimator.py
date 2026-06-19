from datetime import datetime

from backend.app.schemas import VehicleEstimateRequest, VehicleEstimateResponse


def estimate_vehicle_price(vehicle: VehicleEstimateRequest) -> VehicleEstimateResponse:
    """
    Estimate a used vehicle price using a simple rule-based baseline.

    This is not the final machine-learning model.
    It is the first working version so the API can return realistic-looking results.
    """

    current_year = datetime.now().year
    vehicle_age = current_year - vehicle.year

    base_price = 30000
    explanation = []

    # Age adjustment
    age_deduction = vehicle_age * 1200
    base_price -= age_deduction
    explanation.append(f"Vehicle age reduced the estimate by approximately ${age_deduction}.")

    # Odometer adjustment
    odometer_deduction = int(vehicle.odometer / 10000) * 500
    base_price -= odometer_deduction
    explanation.append(
        f"Odometer reading reduced the estimate by approximately ${odometer_deduction}."
    )

    # Condition adjustment
    condition_adjustments = {
        "Excellent": 3000,
        "Good": 1000,
        "Average": -1000,
        "Poor": -3000,
    }

    condition_adjustment = condition_adjustments.get(vehicle.condition, 0)
    base_price += condition_adjustment

    if condition_adjustment >= 0:
        explanation.append(
            f"{vehicle.condition} condition increased the estimate by approximately ${condition_adjustment}."
        )
    else:
        explanation.append(
            f"{vehicle.condition} condition reduced the estimate by approximately ${abs(condition_adjustment)}."
        )

    # Transmission adjustment
    if vehicle.transmission.lower() == "automatic":
        base_price += 500
        explanation.append("Automatic transmission slightly increased the estimate.")

    # Make sure price does not go too low
    estimated_price = max(base_price, 2000)

    min_price = int(estimated_price * 0.9)
    max_price = int(estimated_price * 1.1)

    confidence = "Low"

    return VehicleEstimateResponse(
        estimated_price=estimated_price,
        min_price=min_price,
        max_price=max_price,
        confidence=confidence,
        explanation=explanation,
    )