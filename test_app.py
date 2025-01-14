import pytest
import json
from app import app, mongo

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            # Limpar coleções para testes
            mongo.db.planetas.delete_many({})
            mongo.db.filmes.delete_many({})
        yield client

def test_create_planet(client):
    response = client.post('/planetas', json={
        "nome": "Tatooine",
        "clima": "Arido",
        "diametro": "10465",
        "populacao": "200000"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data

def test_create_film_with_planet(client):
    # Criar planeta
    planet_response = client.post('/planetas', json={
        "nome": "Tatooine",
        "clima": "Arido",
        "diametro": "10465",
        "populacao": "200000"
    })
    planet_id = planet_response.get_json()["id"]

    # Criar filme referenciando planeta
    response = client.post('/filmes', json={
        "titulo": "A New Hope",
        "data_lancamento": "1977-05-25",
        "diretor": "George Lucas",
        "planetas": [planet_id]
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data

def test_get_planets(client):
    response = client.get('/planetas')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0

def test_get_films(client):
    response = client.get('/filmes')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0
