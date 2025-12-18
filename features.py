import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["salary_to_age"] = df["salary"] / df["age"]

    df["age_bucket"] = pd.cut(
        df["age"],
        bins=[0, 30, 45, 120],
        labels=["Young", "Mid", "Senior"]
    )

    return df
