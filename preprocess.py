import pandas as pd

def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Convert raw input JSON into a DataFrame
    """
    df = pd.DataFrame([data])

    return df
