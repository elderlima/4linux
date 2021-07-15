import flask
import sw.dados


# bp = flask.Flask(__name__)
bp = flask.Blueprint("veiculos", __name__, url_prefix="/veiculos")

@bp.route("")
def listar_veiculos():
    return flask.jsonify(sw.dados.veiculos)

@bp.route("", methods=["POST"])
def criar_veiculo():
    veiculo = flask.request.json
    sw.dados.veiculos.append(veiculo)
    id = len(sw.veiculos) - 1
    return flask.jsonify({"id":id})

@bp.route("/<int:id>", methods=["PUT"])
def modificar_veiculo(id):
    veiculo = flask.request.json
    sw.dados.veiculos[id] = veiculo
    return flask.jsonify({"ok": True})