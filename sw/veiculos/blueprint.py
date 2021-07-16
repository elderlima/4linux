import flask
from bson.json_util import dumps
from flask.templating import render_template
from . import models
from config.api import cabecalhos

bp = flask.Blueprint("veiculos", __name__, url_prefix="/veiculos")

@bp.route("")
def index():
    veiculos = list(models.veiculos())
    return flask.render_template("veiculos/index.html",
                                veiculos=veiculos)

@bp.route("/<id>/editar", methods=["GET", "POST"])
def editar_veiculo(id):
    if flask.request.method == 'GET':
        veiculo = models.get_veiculo(id) 
        return flask.render_template("veiculos/edit.html", veiculo=veiculo)
    
    elif flask.request.method == 'POST':
        novo_nome = flask.request.form['veiculo_nome']
        models.modificar_veiculo(id, {'nome': novo_nome})
        return flask.redirect(flask.url_for("veiculos.index"))


@bp.route("api")
def listar_veiculos():
    veiculo = dumps(list(models.veiculos()))
    return flask.Response(veiculo, headers=cabecalhos)

@bp.route("api", methods=["POST"])
def criar_veiculo():
    veiculo = flask.request.json
    result = models.criar_veiculos(veiculo)
    return flask.jsonify({"id": str(result.inserted_id)})

@bp.route("api/<int:id>")
def get_veiculos(id):
    veiculo = dumps(list(models.veiculos())[id])
    return flask.Response(veiculo, headers=cabecalhos)

@bp.route("api/<int:id>", methods=["PUT"])
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