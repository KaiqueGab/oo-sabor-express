import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url) # Makes the GET request

if response.status_code == 200:
    data_json = response.json() # Converts response to JSON
    data_restaurant = {}
    print(response.status_code)

    for item in data_json:
        name_restaurant = item['Company']
        if name_restaurant not in data_restaurant:
            data_restaurant[name_restaurant] = [] # Creates a list for a new restaurant

        # Adds the menu item to the corresponding restaurant
        data_restaurant[name_restaurant].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description'],
        })

    # Saves each restaurant's data in a separate JSON file
    for name_restaurant, data in data_restaurant.items():
        name_file = f'api/{name_restaurant}.json'
        with open(name_file, 'w') as file_restaurant:
            json.dump(data, file_restaurant, indent=4)
    print('Data recovered successfully!')

else:
    print('Failed to recover data. Status Code:', response.status_code)
