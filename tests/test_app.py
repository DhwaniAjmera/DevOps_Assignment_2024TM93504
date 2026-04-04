import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym" in response.data

def test_get_members(client):
    response = client.get('/members')
    assert response.status_code == 200
    data = response.get_json()
    assert type(data) == list
 
def test_add_member(client):
    new_member = {"name": "Alice", "membership": "Platinum"}
    response = client.post('/members', json=new_member)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Alice"