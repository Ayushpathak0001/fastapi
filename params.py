from fastapi import FastAPI
from mockdata import product



app=FastAPI()
@app.get("/")
def home():
    return "Welcome to the home page"

@app.get("/products")
def products():
    return product


#params is of two types Path params and Query params 
#Path param sotres dynamic values in the url such as https://127.0.0.1:8000/products/1
#Here 1 is the dynamic value in the path params

@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    
    #if product is available with the id,return product,lelse return error message
  for oneProduct in product:
      if oneProduct.get("id")==product_id:
          return oneProduct
  return{
      "error:product is not found for this ID."
  }


#Query params are the values you pass in a url after a ? related to the object items to send extra information to an api endpoint
#ex https://127.0.0.1.8000:/product?id=2&product_name=laptop


@app.get("/product")
def user(name:str):
    for item in product:
        if item["product_name"]==name:
            return item
    
    return ("product not found")

@app.get("/details")
def detail(name:str,age:int,nationality:str):
    return (f"Hello {name}, Your age is {age}, Your are from {nationality}")