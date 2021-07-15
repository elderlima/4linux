import flask
from bson.json_util import dumps
from pymongo import results
import sw.dados


# bp = flask.Flask(__name__)
bp = flask.Blueprint("veiculos", __name__, url_prefix="/veiculos")

# @bp.route("")
# def listar_veiculos():
#     return flask.jsonify(sw.dados.veiculos)

@bp.route("")
def listar_veiculos():
    veiculo = dumps(list(sw.dados.veiculos()))
    return flask.Response(veiculo, headers=sw.dados.cabecalhos)

@bp.route("/<int:id>")
def get_veiculos(id):
    veiculo = dumps(list(sw.dados.veiculos())[id])
    return flask.Response(veiculo, headers=sw.dados.cabecalhos)

# @bp.route("", methods=["POST"])
# def criar_veiculo():
#     veiculo = flask.request.json
#     sw.dados.veiculos.append(veiculo)
#     id = len(sw.veiculos) - 1
#     return flask.jsonify({"id":id})

@bp.route("", methods=["POST"])
def criar_veiculo():
    veiculo = flask.request.json
    result = sw.dados.criar_veiculos(veiculo)
    return flask.jsonify({"id": str(result.inserted_id)})

# @bp.route("/<int:id>", methods=["PUT"])
# def modificar_veiculo(id):
#     veiculo = flask.request.json
#     sw.dados.veiculos[id] = veiculo
#     return flask.jsonify({"ok": True})

@bp.route("/<int:id>", methods=["PUT"])
def modificar_veiculo(id):
    veiculo = flask.request.json
    veiculos = list(sw.dados.veiculos())
    veiculo_velha = veiculos[id]
    result = sw.dados.modificar_veiculo(
        {"_id": veiculo_velha["_id"]},
        veiculo
    )
    return flask.jsonify({
            "modificationsa": result.modified_count
    })