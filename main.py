from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Welcome to API Development 101"}

@app.get("/posts")
def get_posts():
    return {"data": "Yours posts are here"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post) # this is printing the pydantic model
    # print(post.title)
    print(post.model_dump()) # this is printing regular python dictionary
    return {"data": post}
    