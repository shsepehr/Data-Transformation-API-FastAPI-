a# Data Transformation API (FastAPI)

## Overview
This project is a **REST API** built with **FastAPI** that transforms raw input data into a **feature-engineered dataset** ready for machine learning models or data analysis. The API receives JSON input, applies preprocessing and feature engineering, and returns the transformed data in JSON format.

> ⚠️ Note: The example data used in this project is for demonstration purposes only. Replace with your own dataset as needed.

---

## Features
- Accepts **JSON input** data via POST requests.
- Performs **data validation** using Pydantic.
- Applies **feature engineering** and preprocessing on the input.
- Returns **JSON output** with new features ready for ML pipelines.
- Modular and extendable design for future integration with ML models.

---

## Getting Started

### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn
- Pandas

Install dependencies using pip:

```bash
pip install fastapi uvicorn pandas
# Data Transformation API (FastAPI)

## Overview
This project is a **REST API** built with **FastAPI** that transforms raw input data into a **feature-engineered dataset** ready for machine learning models or data analysis. The API receives JSON input, applies preprocessing and feature engineering, and returns the transformed data in JSON format.

> ⚠️ Note: The example data used in this project is for demonstration purposes only. Replace with your own dataset as needed.

---

## Features
- Accepts **JSON input** data via POST requests.
- Performs **data validation** using Pydantic.
- Applies **feature engineering** and preprocessing on the input.
- Returns **JSON output** with new features ready for ML pipelines.
- Modular and extendable design for future integration with ML models.

---

## Getting Started

### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn
- Pandas

Install dependencies using pip:

```bash
pip install fastapi uvicorn pandas
Running the API

1.Navigate to the project directory.

2.Start the server using Uvicorn:
uvicorn main:app --reload

By default, the API will run at: http://127.0.0.1:8000

GET / 

Health check to ensure the server is running.
Response example:
{
  "status": "API is running"
}

Transform Data
POST /transform


Accepts JSON input for data transformation.

Example request body:

{
  "age": 32,
  "salary": 62000,
  "department": "IT"
}


Example response:

{
  "age": 32,
  "salary": 62000,
  "department": "IT",
  "salary_to_age": 1937.5,
  "age_bucket": "Mid"
}


Note: The features salary_to_age and age_bucket are generated based on the input values.

Testing via Browser

Open Swagger UI in your browser:

http://127.0.0.1:8000/docs


Interactively test the /transform endpoint.

Optional: Test via HTML (Chrome)

Open test_api.html provided in the project.

Enter values and click Send JSON to see the API response.
