# import flask
# from bson.json_util import dumps
# from pymongo import results
# import sw.dados

import flask
from bson.json_util import dumps
from . import models
from config.api import cabecalhos

bp = flask.Blueprint("veiculos", __name__, url_prefix="/veiculos")

@bp.route("")
def listar_veiculos():
    veiculo = dumps(list(models.veiculos()))
    return flask.Response(veiculo, headers=cabecalhos)

@bp.route("", methods=["POST"])
def criar_veiculo():
    veiculo = flask.request.json
    result = models.criar_veiculos(veiculo)
    return flask.jsonify({"id": str(result.inserted_id)})

@bp.route("/<int:id>")
def get_veiculos(id):
    veiculo = dumps(list(models.veiculos())[id])
    return flask.Response(veiculo, headers=cabecalhos)

@bp.route("/<int:id>", methods=["PUT"])
def modificar_veiculo(id):
    veiculo = flask.request.json
    veiculos = list(models.veiculos())
    veiculo_velha = veiculos[id]
    result = models.modificar_veiculo(
        {"_id": veiculo_velha["_id"]},
        veiculo
    )
    return flask.jsonify({
            "modificationsa": result.modified_count
    })