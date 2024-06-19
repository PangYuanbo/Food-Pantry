from fastapi import HTTPException
from fastapi import Depends
from fastapi import FastAPI,File, UploadFile, Form
import ask_gpt
app = FastAPI()
@app.get("/informain/   ")
def read_informain(
        name: str,
        age: int,
        height: float,
        weight: float,
        files:list[UploadFile] = File(...),
):
    ask_gpt
    return {"name": name, "age": age, "height": height, "weight": weight}


