from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

# Defined my schema below using Pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# Why I am hardcoding dummy posts-- so that everytime program restarts it has something to write on
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}]

@app.get("/")
def root():
    return {"message": "Welcome to API Development 101"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,1000000) # assigning an id, normally DB does it, but here we are using random  
    my_posts.append(post_dict)
    return {"data": post_dict}
    