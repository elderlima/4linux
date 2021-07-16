# import flask
# from bson.json_util import dumps
# from pymongo import results
# import sw.dados

import flask
from bson.json_util import dumps
from . import models
from config.api import cabecalhos

bp = flask.Blueprint("personagens", __name__, url_prefix="/personagens")

@bp.route("")
def listar_personagens():
    personagem = dumps(list(models.personagens()))
    return flask.Response(personagem, headers=cabecalhos)

@bp.route("", methods=["POST"])
def criar_personagem():
    personagem = flask.request.json
    result = models.criar_personagens(personagem)
    return flask.jsonify({"id": str(result.inserted_id)})

@bp.route("<int:id>")
def get_personagens(id):
    personagem = dumps(list(models.personagens())[id])
    return flask.Response(personagem, headers=cabecalhos)

@bp.route("/<int:id>", methods=["PUT"])
def modificar_personagem(id):
    personagem = flask.request.json
    personagens = list(models.personagens())
    personagem_velha = personagens[id]
    result = models.modificar_personagem(
        {"_id": personagem_velha["_id"]},
        personagem
    )
    return flask.jsonify({
            "modificationsa": result.modified_count
    })