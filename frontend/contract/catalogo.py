from pydantic import BaseModel, EmailStr, PositiveFloat, validator
from datetime import date
from enum import Enum


class CategoriaEnum(str, Enum):
    categoria_1 = 'Categoria 1'
    categoria_2 = 'Categoria 2'
    categoria_3 = 'Categoria 3'
    categoria_4 = 'Categoria 4'
    categoria_5 = 'Categoria 5'
    categoria_6 = 'Categoria 6'
    categoria_7 = 'Categoria 7'
    categoria_8 = 'Categoria 8'
    categoria_9 = 'Categoria 9'
    


class Catalogo(BaseModel):
    EAN: int
    Produto: str
    Categoria: CategoriaEnum
    Descrição: str
    Preço: PositiveFloat
    Fornecedor: EmailStr
    Data: date

@validator("Preço")
def validate_preco(cls, value):
    if value < 0:
        raise ValueError("Preço não pode ser negativo")
    return value