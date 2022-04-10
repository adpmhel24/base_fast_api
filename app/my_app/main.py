from multiprocessing import context
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
def index():
    return {"title": "Welcome"}
