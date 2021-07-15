import flask
import sw.dados

# bp = flask.Flask(__name__)
bp = flask.Blueprint("personagens", __name__, url_prefix="/personagens")

@bp.route("")
def listar_personagens():
    return flask.jsonify(sw.dados.personagens)

@bp.route("<int:id>")
def get_personagens(id):
    return flask.jsonify(sw.dados.personagens[id])

@bp.route("", methods=["POST"])
def criar_personagem():
    personagem = flask.request.json
    sw.dados.personagens.append(personagem)
    id = len(sw.dados.personagens) - 1
    return flask.jsonify({"id":id})

@bp.route("<int:id>", methods=["PUT"])
def modificar_personagem(id):
    personagem = flask.request.json
    sw.dados.personagens[id] = personagem
    return flask.jsonify({"ok": True})