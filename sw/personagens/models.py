from bson.objectid import ObjectId
from config.db import db

def personagens():
    return db.personagens.find()

def get_personagem(oid):
    filtro = {"_id": ObjectId(oid)}
    return db.personagens.find_one(filtro)

def criar_personagens(personagem):
    return db.personagens.insert_one(personagem)

def modificar_personagem(oid, personagem):
    if isinstance(oid, str):
        oid = {"_id": ObjectId(oid)}
    return db.personagens.update_one(
        oid,
        {"$set": personagem}
    )