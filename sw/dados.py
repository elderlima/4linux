import pymongo

cliente = pymongo.MongoClient()

cabecalhos = {"Content-Type": "application/json"}

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

    db = cliente["sw"]

    if db.naves.count() > 0:
        return

    db.naves.insert_many(naves)
    db.personafens.insert_many(personagens)
    db.veiculos.insert_many(veiculos)

def naves():
    db = cliente.sw
    return db.naves.find()

def criar_naves(nave):
    db = cliente.sw
    return db.naves.insert_one(nave)

def modificar_naves(oid, nave):
    return cliente.sw.naves.update_one(
        oid,
        {"$set": nave}
    )