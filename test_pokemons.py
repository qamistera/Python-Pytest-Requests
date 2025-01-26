import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKKEN = '7e6eb17127ec9bb4c87a6ddb0e051c7c'
HEADER ={'Content-Type': 'application/json'}
TRAINER_ID = 19777

def test_get_trainers_status_code():
    response = requests.get(url=f'{URL}/trainers', params= {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_get_trainers_status_code():
    response = requests.get(url=f'{URL}/trainers', params= {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

    data = response.json()
    trainer_name = data['data'][0]['trainer_name']  # Получаю имя тренера из ответа
    assert trainer_name == 'ZoRRo'    