import flask
from bson.json_util import dumps
from pymongo import results
import sw.dados

# bp = flask.Flask(__name__)
bp = flask.Blueprint("personagens", __name__, url_prefix="/personagens")

@bp.route("")
def listar_personagens():
    personagem = dumps(list(sw.dados.personagens()))
    return flask.Response(personagem, headers=sw.dados.cabecalhos)
    # return flask.jsonify(sw.dados.personagens)

@bp.route("<int:id>")
def get_personagens(id):
    personagem = dumps(list(sw.dados.personagens())[id])
    return flask.Response(personagem, headers=sw.dados.cabecalhos)
    # return flask.jsonify(sw.dados.personagens[id])

# @bp.route("", methods=["POST"])
# def criar_personagem():
#     personagem = flask.request.json
#     sw.dados.personagens.append(personagem)
#     id = len(sw.dados.personagens) - 1
#     return flask.jsonify({"id":id})

@bp.route("", methods=["POST"])
def criar_personagem():
    personagem = flask.request.json
    result = sw.dados.criar_personagens(personagem)
    return flask.jsonify({"id": str(result.inserted_id)})

# @bp.route("<int:id>", methods=["PUT"])
# def modificar_personagem(id):
#     personagem = flask.request.json
#     sw.dados.personagens[id] = personagem
#     return flask.jsonify({"ok": True})

@bp.route("/<int:id>", methods=["PUT"])
def modificar_personagem(id):
    personagem = flask.request.json
    personagens = list(sw.dados.personagens())
    personagem_velha = personagens[id]
    result = sw.dados.modificar_personagem(
        {"_id": personagem_velha["_id"]},
        personagem
    )
    return flask.jsonify({
            "modificationsa": result.modified_count
    })