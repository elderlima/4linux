from bson.objectid import ObjectId
from config.db import db

def naves():
    return db.naves.find()

def get_nave(oid):
    filtro = {"_id": ObjectId(oid)}
    return db.naves.find_one(filtro)

def criar_naves(nave):
    return db.naves.insert_one(nave)

def modificar_naves(oid, nave):
    if isinstance(oid, str):
        oid = {"_id": ObjectId(oid)}
    return db.naves.update_one(
        oid,
        {"$set": nave}
    )