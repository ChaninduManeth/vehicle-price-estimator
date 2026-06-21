# Vehicle Price Estimator

A full-stack application that estimates the market value of a used
vehicle based on its specifications, condition and market information.

## Project Status

Early development — backend foundation completed and the first baseline estimation endpoint is working.

## Planned Technology Stack

- React and Vite
- Python and FastAPI
- Pandas
- Scikit-learn
- PostgreSQL
- Azure
- GitHub Actions

## Current Backend Features

- FastAPI backend setup
- Health-check endpoint
- Vehicle price estimation endpoint
- Request and response validation using Pydantic schemas
- Rule-based baseline estimator
- Price range output
- Confidence level output
- Explanation of pricing factors

## Planned Features

- Vehicle information form
- Estimated market price
- Estimated price range
- Confidence level
- Explanation of important pricing factors
- Dataset-based comparison logic
- Machine-learning price prediction
- Similar vehicle comparisons
- Cloud deployment

## Repository Structure

- `backend/` — FastAPI backend
- `frontend/` — React frontend
- `data/` — raw and processed vehicle data
- `notebooks/` — data exploration and model development
- `models/` — trained machine-learning models
- `docs/` — project documentation
- `tests/` — automated tests

## Current Progress

- [x] GitHub repository created
- [x] Initial project structure created
- [x] FastAPI backend started
- [x] Health-check endpoint added
- [x] Vehicle input schema
- [x] Baseline price estimator
- [ ] Kaggle dataset added locally
- [ ] Initial data analysis notebook
- [ ] Data cleaning pipeline
- [ ] Machine-learning model
- [ ] React frontend
- [ ] Cloud deployment