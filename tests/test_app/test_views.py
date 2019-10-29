from rest_framework.status import HTTP_201_CREATED


def test_index(client):
    response = client.get('/index/')
    assert response.status_code == HTTP_201_CREATED
