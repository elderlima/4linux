import pymongo
import random

client = pymongo.MongoClient()
db = client.loja

def setup():
    produtos = [
        {"nome": "Headset", "preço":279.90},
        {"nome": "RX 6700", "preço":5899.90},
        {"nome": "Mouse Reddragon", "preço":119.90},
        {"nome": "Xbox S", "preço":2519.90},
        {"nome": "Galaxy M12", "preço":1709.05},
        {"nome": "Memoria XPG", "preço":317.90},
        {"nome": "Monitor Gamer", "preço":1499.90},
        {"nome": "Notebook Gamer", "preço":5099.00},
        {"nome": "Teclado Gamer", "preço":299.90},
        ]

    if db.produtos.count() > 0:
        return
    
    for produto in produtos:
        produto["estoque"] = random.randint(0, 99)

    db.produtos.insert_many(produtos)