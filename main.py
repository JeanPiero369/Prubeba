from fastapi import FastAPI,Response
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    stock:bool=True

items=[]

@app.post("/items")
def add_item(item:Item,response:Response):
    item=item.append(item)
    response.status_code=201
    return{"item":item}

@app.get("/items")
def items():
    return items

