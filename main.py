from fastapi import HTTPException
from fastapi import Depends
from fastapi import FastAPI

app = FastAPI()
@app.get("/informain")
def read_informain(
        name: str,
        age: int,
        height: float,
        weight: float,
        sex: str,
):
    return {"name": name, "age": age, "height": height, "weight": weight}


