import pymongo

cliente = pymongo.MongoClient()
db = cliente.sw

def setup():
    naves = [
        {"nome":"x-wing"},
        {"nome":"Y-wing"}
    ]

    personagens = [
        {"nome":"Lucas Andarilhos do Ceu"},
        {"nome":"Leia dos Órgãos"}
    ]

    veiculos = [
        {"nome":"Fusca"},
        {"nome":"Belinda"}
    ]

    if db.naves.count() > 0:
        return
    
    if db.personagens.count() > 0:
        return

    if db.veiculos.count() > 0:
        return

    db.naves.insert_many(naves)
    db.personagens.insert_many(personagens)
    db.veiculos.insert_many(veiculos)