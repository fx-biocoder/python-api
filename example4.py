from fastapi import FastAPI, Query, HTTPException, status
from typing import Optional 
from pydantic import BaseModel

app = FastAPI()

# Create an Item class that inherits from BaseModel
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: str = None
    price: float = None
    brand: Optional[str] = None

# Endpoint '/'
# HTTP Method: GET
@app.get('/')
def home():
    return {'Data':'test'}

# Endpoint '/about'
# HTTP Method: GET
@app.get('/about')
def about():
    return {'Another':'dict'}

# Inventory with items
# Syntax -> { id: {product-dictionary} } (dict inside dict)
inventory = {
        1 : {
            'name': 'Product1',
            'price': 10,
            'brand': 'Brand 1'
        },
        2 : {
            'name': 'Product2',
            'price': 20,
            'brand': 'Brand 2'
        }
}

# Accepting query parameters in an endpoint
# Default value is None if we do not specify a query parameter
# name is optional
# Ejemplo de petición: 127.0.0.1:8000/get-by-name?name='Product2'
@app.get('/get-by-name')
def get_item(*args, name: Optional[str] = None, description='Name of the item'):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Item ID not found.')

# Request body
# POST 
# Create new item for the inventory
@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail='Item ID already exists')
    
    inventory[item_id] = item
    return inventory[item_id]

# Update element
# PUT method
@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Item ID not found.')
    
    if item.name != None:
        inventory[item_id].name = item.name
    
    if item.price != None:
        inventory[item_id].price = item.price
    
    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

# Delete element
# DELETE method
@app.delete('/delete-item')
def delete_item(item_id: int = Query(..., description='The ID of the item to delete')):
    if item_id not in inventory:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Item ID not found.')
    
    del inventory[item_id]
    return {'Success': 'Item deleted'}