import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'cinema.settings'
django.setup() 

import pytest
from ninja.testing import TestClient
from .api import app

client = TestClient(app)

@pytest.mark.django_db
def test_create_movie():
    response = client.post("",json={"name": "Pytagon","protagonist":"Python","poster":"/media/media/s-l1600.jpg","trailer": "https://youtu.be/LWwo5PeIF-Y?si=GhzOetNJYgi5F913","start_date":"2024-03-12T00:00:00Z","status":"coming_up","ranking":4})
    assert response.status_code == 200

@pytest.mark.django_db
def test_list():
    response = client.get("")
    assert response.status_code == 200
    assert len(response.json()) == 6