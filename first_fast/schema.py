# file para criar um contrato (schema), de como sera enviado os dados na API


from pydantic import BaseModel

class Message(BaseModel):
    message: str
