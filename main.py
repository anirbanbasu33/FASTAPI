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
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favourite foods 1", "content": "I like pizza", "id": 2}]


def find_post(id):
    for i in my_posts:
        if i["id"] == id:
            return i
            

@app.get("/")
def root():
    return {"message": "Welcome to API Development 101"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


## Retrieving one individual post
@app.get("/posts/{id}")  # id = path parameter...everytime we get a path parameter, even if its a number, it will be returned as a string...therefore we must manually convert it to an integer
def get_post(id: int):   # Doing the above data validation
    # print(type(id))
    post = find_post(id)
    print(post)
    return {"post_detail": post}


@app.post("/posts")
def create_posts(post: Post): # Data validation with above Class
    post_dict = post.model_dump() # to_dict()
    post_dict['id'] = randrange(0,1000000) # assigning an id, normally DB does it, but here we are using random  
    my_posts.append(post_dict)
    return {"data": post_dict}
    
