from fastapi import FastAPI, Request
from mockdata import products
from dtos import ProductDTO

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to FASTAPI Series!"

@app.get("/connect")
def contact():
    return "You can connect us any time!"

@app.get("/products")
def get_products():
    return products

# PATH PARAMS
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct
    return {
        "error": "Product not found for this id."
    }

# QUERY PARAMS
# @app.get("/greet")
# def greet_user(name:str, age:int):
#     return {
#         "greet": f"Hello {name}, Your age is {age}."
#     }

@app.get("/greet")
def greet_user(request:Request):
    query_params = dict(request.query_params)
    return {
        "greet": f"Hello {query_params.get("name")}, Your age is {query_params.get("age")}."
    }

# Different types of HTTP Methods

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"status":"Product created successfully...", "data":products}

def update_product(product_data:ProductDTO, product_id:int):
    for oneProduct in products:
        
    return {"status" : "Product updated successfully"}
# Body, Headers - Request Headers, Query Params


# print(fastapi.__version__)
# fastapi dev main.py
# fastapi dev main.py --RELOAD