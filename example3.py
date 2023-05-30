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

#Using query parameters AND path parameters at the same time
@app.get('/get-item/{item_id}')
def get_item(*args, item_id: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
        
    return {'Data':'Not found'}