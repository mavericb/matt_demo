########## main.py ##########

from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/submit")
async def submit(input: Input):
    return {"message": f"Data submitted is: {input.text}"}
#