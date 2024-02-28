from pydantic import BaseModel

class Input(BaseModel):
    text: str

class InputModel(BaseModel):
    input: str
    perfect_factors: str