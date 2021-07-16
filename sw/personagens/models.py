from config.db import db

def personagens():
    # db = cliente.sw
    return db.personagens.find()

def criar_personagens(personagem):
    # db = cliente.sw
    return db.personagens.insert_one(personagem)

def modificar_personagem(oid, personagem):
    return db.personagens.update_one(
        oid,
        {"$set": personagem}
    )

