from fastapi import FastAPI
from Hello import Hello

app = FastAPI()


@app.get("/testjenkins")
def read_root():
    return Hello.Hello_World()