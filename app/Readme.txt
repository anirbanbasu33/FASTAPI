## SETTING UP THE VIRTUAL ENVIRONMENT

python3 -m venv <name of venv>
# Setting up seperate interpreter for our venv
view - command pallete - pythn:select interpreter - enter interpreter path --> ./venv/bin/python
# Enabling venv for our command pallete-
source venv/bin/activate 
# Install necessary libraries
pip install "fastapi[all]"


## STARTING THE FAST API PROGRAM

uvicorn main:app --reload

(main = filename, app = name of our fastapi within main)


## Used pydantic for setting up schema/data validation
# Defined my schema below using Pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


## FAST API'S OWN DOCUMENTATION

http://127.0.0.1:8000/docs (using swagger)
http://127.0.0.1:8000/redoc


## CREATED NEW PYTHON PACKAGE
Created 'app' folder inside FASTAPI parent folder, created a file '__init__.py', standard file to create package
Moved main.py inside the app folder

uvicorn app.main:app --reload
(uvicorn looks inside app directory for a file called main, and within main look for our fastapi instance- app )



## DATABASES
Relational and NonRelational DB
- Using Postgres
- We are creating one individual db for our application

## GIT commands
git init
git status
git add main.py
git status
git commit -m "your commit name"
git branch -M main
git remote add origin https://github.com/anirbanbasu33/FASTAPI.git
git push -u origin main