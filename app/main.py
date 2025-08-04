from fastapi import FastAPI, Response, status, HTTPException
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


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favourite foods 1", "content": "I like pizza", "id": 2}]


def find_post(id):
    for i in my_posts:
        if i["id"] == id:
            return i
        
def find_index_post(id):
    for index, element in enumerate(my_posts):
        if element["id"] == id:
            return index
            
            
## HOME
@app.get("/")
def root():
    return {"message": "Welcome to API Development 101"}


## GETTING ALL POSTS
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


## CREATING POSTS
# Change the status code=201,inside decorator once something is created
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): 
    post_dict = post.model_dump() 
    post_dict['id'] = randrange(0,1000000) 
    my_posts.append(post_dict)
    return {"data": post_dict}

## GETTING THE LATEST POST
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

## GETTING AN INDIVIDUAL POST
@app.get("/posts/{id}")  
def get_post(id: int):   ## storing the response code I get in 'response' var
    
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    return {"post_detail": post}

## DELETING A POST
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
## UPDATING A POST
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID: {id} does not exist")
    
    post_dict = post.model_dump() # Convert the data from frontend to a python dictionary
    post_dict['id'] = id # Add the id into the dictionary
    my_posts[index] = post_dict # Update that specific spot in the array
    return {"data": post_dict}


# Adding a line
