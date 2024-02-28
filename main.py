from fastapi import FastAPI
from demo import overall_chain
from models import Input, InputModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/submit")
async def submit(input: Input):
    return {"message": f"Data submitted is: {input.text}"}

@app.post("/generate-solutions/")
async def generate_solutions(data: InputModel):
    try:
        result = overall_chain({"input": data.input, "perfect_factors": data.perfect_factors})
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
