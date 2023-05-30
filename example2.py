from fastapi import FastAPI, Path
from typing import Optional # For when you pass an optional parameter

app = FastAPI()

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

# Get item
# Path -> default value is None if you do not pass an item_id
# Greater than 0 (I don't have item id 0)
# Lesser than 3 (I don't have item id 3)
@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description='The ID of the product you want to view', gt=0, lt=3)): 
    return inventory[item_id]       

# Accepting query parameters in an endpoint
# Default value is None if we do not specify a query parameter
# name is optional
# Ejemplo de petición: 127.0.0.1:8000/get-by-name?name='Product2'
@app.get('/get-by-name')
def get_item(*args, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
        
    return {'Data':'Not found'}
