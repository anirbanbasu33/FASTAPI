# v3
from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to API Development 101"}

@app.get("/posts")
def get_posts():
    return {"data": "Yours posts are here"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    print(payLoad["title"])
    return {"message": payLoad}