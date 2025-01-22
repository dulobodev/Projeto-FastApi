from http import HTTPStatus

from fastapi.testclient import TestClient

from first_fast.cod import app


def test_read_root_deve_retornar_OK_ola_mundo():
    client = TestClient(app)

    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
