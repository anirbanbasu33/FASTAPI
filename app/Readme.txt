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
uvicorn app.main:app --reload



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

## psycopg2 lib doesnot include column names, only column values, must pass an extra field to get column names
from psycopg2.extras import RealDictCursor
...
cursor_factory=RealDictCursor (Just gives the column name)




## GIT commands
git init
git status
git add main.py
git status
git commit -m "your commit name"
git branch -M main
git remote add origin https://github.com/anirbanbasu33/FASTAPI.git





###  POSTGRESQL COMMANDS HISTORY
SELECT * FROM products;

-- SELECT id FROM products;
-- SELECT id AS products_id, is_sale AS on_sale FROM products;
-- select * from products where id = 9;
-- SELECT * FROM products WHERE inventory != 0;
-- SELECT * FROM products WHERE name LIKE 'C%';
-- SELECT * FROM products WHERE name LIKE '%cil';

-- SELECT * FROM products WHERE price >= 80;
-- SELECT * FROM products WHERE inventory <> 0;
-- SELECT * FROM products WHERE inventory > 0 AND price >250;
-- SELECT * FROM products WHERE inventory > 0 AND price >100 OR price <20;
-- SELECT * FROM products WHERE id IN (1,2,3);

SELECT * FROM products WHERE name LIKE 'TV%'; 
SELECT * FROM products WHERE name not LIKE 'TV%';
SELECT * FROM products WHERE name LIKE '%en%';
select * from products order by price;
select * from products order by price desc;
select * from products order by inventory desc;
select * from products order by inventory desc, price;

select * from products order by created_at desc;
select * from products where price > 20 order by created_at desc;

SELECT * FROM products LIMIT 10;
SELECT * FROM products WHERE price > 10 LIMIT 3;


-- check first 5 records
select * from products order by id limit 5;

-- skip a certain number of rows use offset-----PAGINATION IN API
select * from products order by id limit 5 offset 2;

-- INSERT DATA
INSERT INTO products (name, price, inventory ) VALUES ('tortilla', 4, 1000);

SELECT * FROM products;
INSERT INTO products (price, name, inventory ) VALUES (4, 'tortilla', 1000);
select * from products where name = 'tortilla';

-- Creates the entry and returns a response
INSERT INTO products (price, name, inventory ) VALUES (10000, 'cars', 1000), (50, 'laptop', 25), (60, 'monitor', 4) returning *;

-- Creates the entry and returns a response
INSERT INTO products (price, name, inventory ) VALUES (10000, 'cars', 1000), (50, 'laptop', 25), (60, 'monitor', 4) returning id, created_at, name;


-- DELETE DATA
DELETE FROM products WHERE id = 10; 
SELECT * FROM products;
DELETE FROM products WHERE id = 11 RETURNING *; 


-- UPDATING ROWS
SELECT * FROM products;
UPDATE products SET name = 'flour tortilla', price = 40 WHERE id = 22 ; 
UPDATE products SET is_sale = true WHERE id = 24 RETURNING * ; 
UPDATE products SET is_sale = true WHERE id > 15 RETURNING * ;
