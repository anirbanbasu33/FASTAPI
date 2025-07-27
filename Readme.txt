## SETTING UP THE VIRTUAL ENVIRONMENT

python3 -m venv <name of venv>
# Setting up seperate interpreter for our venv
view - command pallete - pythn:select interpreter - enter interpreter path --> ./venv/bin/python
# Enabling venv for our command pallete-
source venv/bin/activate 


## STARTING THE FAST API PROGRAM

uvicorn main:app --reload


##