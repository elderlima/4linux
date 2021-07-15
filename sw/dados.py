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
    
    if db.personagens.count() > 0:
        return

    if db.veiculos.count() > 0:
        return

    db.naves.insert_many(naves)
    db.personagens.insert_many(personagens)
    db.veiculos.insert_many(veiculos)

def naves():
    db = cliente.sw
    return db.naves.find()

def personagens():
    db = cliente.sw
    return db.personagens.find()

def veiculos():
    db = cliente.sw
    return db.veiculos.find()

def criar_naves(nave):
    db = cliente.sw
    return db.naves.insert_one(nave)

def criar_personagens(personagem):
    db = cliente.sw
    return db.personagens.insert_one(personagem)

def criar_veiculos(veiculo):
    db = cliente.sw
    return db.veiculos.insert_one(veiculo)

def modificar_naves(oid, nave):
    return cliente.sw.naves.update_one(
        oid,
        {"$set": nave}
    )

def modificar_personagem(oid, personagem):
    return cliente.sw.personagens.update_one(
        oid,
        {"$set": personagem}
    )

def modificar_veiculo(oid, veiculo):
    return cliente.sw.veiculos.update_one(
        oid,
        {"$set": veiculo}
    )