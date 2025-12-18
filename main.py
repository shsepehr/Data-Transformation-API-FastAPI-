from fastapi import FastAPI
import pandas as pd

from schemas import InputData, TransformedData
from preprocess import preprocess_input
from features import create_features

app = FastAPI(
    title="Data Transformation API",
    description="API for transforming raw input data into feature-engineered format",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/transform", response_model=TransformedData)
def transform_data(input_data: InputData):

    # Convert input to DataFrame
    df = preprocess_input(input_data.dict())

    # Apply feature engineering
    df = create_features(df)

    # Convert back to dict
    output = {
        "age": int(df.loc[0, "age"]),
        "salary": float(df.loc[0, "salary"]),
        "department": df.loc[0, "department"],
        "salary_to_age": float(df.loc[0, "salary_to_age"]),
        "age_bucket": str(df.loc[0, "age_bucket"])
    }

    return output
