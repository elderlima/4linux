import flask
from bson.json_util import dumps
from pymongo import results
import sw.dados

# app = flask.Flask(__name__)
bp = flask.Blueprint("naves", __name__, url_prefix="/naves")

@bp.route("")
def listar_naves():
    naves = dumps(list(sw.dados.naves()))
    return flask.Response(naves, headers=sw.dados.cabecalhos)
    # return flask.jsonify(naves)

@bp.route("/<int:id>")
def get_nave(id):
    naves = dumps(list(sw.dados.naves())[id])
    return flask.Response(naves, headers=sw.dados.cabecalhos)

@bp.route("", methods=["POST"])
def criar_nave():
    nave = flask.request.json
    result = sw.dados.criar_naves(nave)
    # id = len(sw.dados.naves) - 1
    return flask.jsonify({"id": str(result.inserted_id)})

# @bp.route("", methods=["POST"])
# def criar_nave():
#     nave = flask.request.json
#     sw.dados.naves.append(nave)
#     id = len(sw.dados.naves) - 1
#     return flask.jsonify({"id":id})

@bp.route("/<int:id>", methods=["PUT"])
def modificar_nave(id):
    nave = flask.request.json
    naves = list(sw.dados.naves())
    # sw.dados.naves[id] = nave
    nave_velha = naves[id]
    result = sw.dados.modificar_naves(
        {"_id": nave_velha["_id"]},
        nave
    )
    return flask.jsonify({
            "modificationsa": result.modified_count
    })
    