from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    salary: float
    department: str


class TransformedData(BaseModel):
    age: int
    salary: float
    department: str
    salary_to_age: float
    age_bucket: str
