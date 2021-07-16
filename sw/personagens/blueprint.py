import flask
from bson.json_util import dumps
from flask.templating import render_template
from . import models
from config.api import cabecalhos

bp = flask.Blueprint("personagens", __name__, url_prefix="/personagens")

@bp.route("")
def index():
    personagens = list(models.personagens())
    return flask.render_template("personagens/index.html",
                                personagens=personagens)

@bp.route("/<id>/editar", methods=["GET", "POST"])
def editar_personagem(id):
    if flask.request.method == 'GET':
        personagem = models.get_personagem(id) 
        return flask.render_template("personagens/edit.html", personagem=personagem)
    
    elif flask.request.method == 'POST':
        novo_nome = flask.request.form['personagem_nome']
        models.modificar_personagens(id, {'nome': novo_nome})
        return flask.redirect(flask.url_for("personagens.index"))

@bp.route("api")
def listar_personagens():
    personagem = dumps(list(models.personagens()))
    return flask.Response(personagem, headers=cabecalhos)

@bp.route("api", methods=["POST"])
def criar_personagem():
    personagem = flask.request.json
    result = models.criar_personagens(personagem)
    return flask.jsonify({"id": str(result.inserted_id)})

@bp.route("api/<int:id>")
def get_personagens(id):
    personagem = dumps(list(models.personagens())[id])
    return flask.Response(personagem, headers=cabecalhos)

@bp.route("api/<int:id>", methods=["PUT"])
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