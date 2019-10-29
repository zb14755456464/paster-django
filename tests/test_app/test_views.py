from pytest import mark
from rest_framework.status import HTTP_201_CREATED


def test_index(client):
    response = client.get('/index/')
    assert response.status_code == HTTP_201_CREATED


@mark.django_db
def test_human(client):
    response = client.post('/human/')
    assert response.status_code == HTTP_201_CREATED
