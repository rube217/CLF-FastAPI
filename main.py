
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"Hello":"World"} 

@app.post("/person/new")
def create_person():
    pass
