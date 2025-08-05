from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint that shows an amazing message from the programming world!
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurants/')
def get_restaurant(restaurant: str=Query(None)):
    '''
    Endpoint that shows the menu of restaurants.
    If a restaurant name is provided, returns only its menu.
    '''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    response = requests.get(url)  # Makes a GET request to the API

    if response.status_code == 200:
        data_json = response.json()  # Converts the response to JSON
        if restaurant is None:
            return {'Dados': data_json}  # Returns all data if no restaurant is specified

        data_restaurant = []
        for item in data_json:
            if item['Company'] == restaurant:
                # Adds menu items for the specified restaurant
                data_restaurant.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description'],
            })
        return {'Restaurant':restaurant, 'Cardapio':data_restaurant}
    else:
        # Returns error if the request fails
        return {'Error':f'{response.status_code} - {response.text}'}