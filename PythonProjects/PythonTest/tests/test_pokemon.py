import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4814560b6b07925fe42d107af6779732'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '7656'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_id"] == TRAINER_ID