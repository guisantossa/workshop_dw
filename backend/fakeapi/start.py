from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI()
fake = Faker()

file_name = 'backend/fakeapi/products.csv'
df = pd.read_csv(file_name)
df['indice'] = range(1, len(df) + 1)
df.set_index('indice', inplace=True)

@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]
    return [{
        "client" : fake.name(),
        "creditcard": fake.credit_card_number(),
        "product": tuple['products'],
        "ean": int(tuple['ean']),
        "price": round(float(tuple['price']*1.2),2),
        "store": 11,
        "dateTime": fake.iso8601(),
        "clientPosition": fake.location_on_land()
    }]

@app.get("/gerar_compras/{quantidade}")
async def gerar_compras(quantidade: int):
    if quantidade <1:
        return {"error": "Quantidade inválida, número deve ser maior que 1"}
    
    respostas = []
    for i in range(quantidade):
        index = random.randint(1, len(df)-1)
        tuple = df.iloc[index]
        pessoa =  {
            "client" : fake.name(),
            "creditcard": fake.credit_card_number(),
            "product": tuple['products'],
            "ean": int(tuple['ean']),
            "price": round(float(tuple['price']*1.2),2),
            "store": 11,
            "dateTime": fake.iso8601(),
            "clientPosition": fake.location_on_land()
        }
        respostas.append(pessoa)
    return respostas

