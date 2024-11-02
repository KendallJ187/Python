import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4814560b6b07925fe42d107af6779732'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
BODY_POK = {
    "name": "Бульбазавр",
    "photo_id": 1
}
BODY_RENAME = {
    "pokemon_id": "12331",
    "name": "New Name",
    "photo_id": 2
}
BODY_CATCH = {
    "pokemon_id": "9"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_POK)
print(response_create.text)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_RENAME)
print(response_rename.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CATCH)
print(response_catch.text)
