import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKKEN = ''
HEADER ={'Content-Type': 'application/json', 'trainer_token' : TOKKEN}


body_create_p ={
    "name": "generate",
    "photo_id": -1
}

body_change_p ={
    "pokemon_id": "204573",
    "name": "HabaHaba",
    "photo_id": 2
}

body_add_pokeball={
    "pokemon_id": "204576"
}

response_create_p = requests.post(url=f'{URL}/pokemons', headers=HEADER,json=body_create_p)

print(response_create_p.text)


response_change_p = requests.put(url=f'{URL}/pokemons', headers=HEADER,json=body_change_p)

print(response_change_p.text)


response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER,json=body_add_pokeball)

print(response_add_pokeball.text)




