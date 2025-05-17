from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, schema de dados, protocolo
    name: str
    type: str

    class Config:
      orm_mode = True