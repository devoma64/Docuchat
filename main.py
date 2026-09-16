from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"home": "Welcome to FastAPI"}
