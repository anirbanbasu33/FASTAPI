from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()

# Defined my schema below using Pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='Piglet@1', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection is successful!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)



# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favourite foods 1", "content": "I like pizza", "id": 2}]
# def find_post(id, posts):
#     for i in posts:
#         if i['id'] == id:
#             return i      
# def find_index_post(id):
#     for index, element in enumerate(my_posts):
#         if element["id"] == id:
#             return index
            
            
## HOME
@app.get("/")
def root():
    return {"message": "Welcome to API Class"}


## GETTING ALL POSTS
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}


## CREATING POSTS
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): 
    cursor.execute("""INSERT INTO posts (title, content, published ) VALUES (%s, %s, %s) RETURNING * """,
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()

    conn.commit()
    return {"data": new_post}


## GETTING THE LATEST POST
@app.get("/posts/latest")
def get_latest_post():
    cursor.execute("""select * from posts ORDER BY created_at DESC LIMIT 1""")
    latest = cursor.fetchone()
    return {"detail": latest}


## GETTING AN INDIVIDUAL POST
@app.get("/posts/{id}")  
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),)) ## adding , for superstition
    post = cursor.fetchone() 
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    return {"post_detail": post}

    

## DELETING A POST
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID: {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

## UPDATING A POST
@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                   (post.title, post.content, post.published, str(id)))
    
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID: {id} does not exist")

    return {"data": updated_post}

