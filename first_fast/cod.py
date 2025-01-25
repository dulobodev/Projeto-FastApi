from fastapi import FastAPI

from http import HTTPStatus

from first_fast.schema import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model= Message)
def read_root():
    return {'message': 'Olá Mundo!'}