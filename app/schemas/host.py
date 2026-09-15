from pydantic import BaseModel


class HostCreate(BaseModel):
    nome: str
    endereco_ip: str