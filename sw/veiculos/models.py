from config.db import db

def veiculos():
    # db = cliente.sw
    return db.veiculos.find()
    
def criar_veiculos(veiculo):
    # db = cliente.sw
    return db.veiculos.insert_one(veiculo)

def modificar_veiculo(oid, veiculo):
    return db.veiculos.update_one(
        oid,
        {"$set": veiculo}
    )
