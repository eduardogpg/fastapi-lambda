from fastapi import FastAPI

from mangum import Mangum

app = FastAPI() 

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.get("/ping")
def hello_world():
    return {"message": "Pong"}


handler = Mangum(app)