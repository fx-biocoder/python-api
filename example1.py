from fastapi import FastAPI

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
            'name': 'Product 1',
            'price': 10,
            'brand': 'Brand 1'
        },
        2 : {
            'name': 'Product 2',
            'price': 20,
            'brand': 'Brand 2'
        }
}

# Let the user retrieve a product based on the id and name
# We tell the function that the id and the name must be integer and string, respectively
# The example does not make sense but it shows how you can pass multiple parameters
@app.get('/get-item/{item_id}/{name}')
def getItem(item_id: int, name: str): 
    return inventory[item_id]       # Returns the product

