from bson.objectid import ObjectId
from config.db import db

def veiculos():
    return db.veiculos.find()

def get_veiculo(oid):
    filtro = {"_id": ObjectId(oid)}
    return db.veiculos.find_one(filtro)
    
def criar_veiculos(veiculo):
    return db.veiculos.insert_one(veiculo)

def modificar_veiculo(oid, veiculo):
    if isinstance(oid, str):
        oid = {"_id": ObjectId(oid)}
    return db.veiculos.update_one(
        oid,
        {"$set": veiculo}
    )
