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


## Used pydantic for setting up schema/data validation


## GIT commands
git init
git status
git add main.py
git status
git commit -m "your commit name"
git branch -M main
git remote add origin https://github.com/anirbanbasu33/FASTAPI.git
git push -u origin main