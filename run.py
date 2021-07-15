import flask
import sw.dados
import sw.naves
import sw.personagens
import sw.veiculos

app = flask.Flask(__name__)
app.register_blueprint(sw.naves.bp)
app.register_blueprint(sw.personagens.bp)
app.register_blueprint(sw.veiculos.bp)

if __name__ == "__main__":
    sw.dados.setup()
    app.run(debug=True)

# @app.route("/naves", methods=["POST"])
# def criar_nave():
#     nave = flask.request.json
#     sw.naves.append(nave)
#     id = len(sw.naves) - 1
#     return flask.jsonify({"id":id})

# @app.route("/naves/<int:id>", methods=["PUT"])
# def modificar_nave(id):
#     nave = flask.request.json
#     sw.naves[id] = nave
#     return flask.jsonify({"ok": True})

# @app.route("/naves", methods=["POST"])
# def apenas_post():
#     return ''

# @app.route("/personagens")
# def listar_personagens():
#     return flask.jsonify(sw.personagens)

# @app.route("/personagens/<int:id>")
# def get_personagens(id):
#     return flask.jsonify(sw.personagens[id])

# @app.route("/personagens", methods=["POST"])
# def criar_personagem():
#     personagem = flask.request.json
#     sw.personagens.append(personagem)
#     id = len(sw.personagens) - 1
#     return flask.jsonify({"id":id})

# @app.route("/personagens/<int:id>", methods=["PUT"])
# def modificar_personagem(id):
#     personagem = flask.request.json
#     sw.personagens[id] = personagem
#     return flask.jsonify({"ok": True})


# @app.route("/veiculos")
# def listar_veiculos():
#     return flask.jsonify(sw.veiculos)

# @app.route("/veiculos", methods=["POST"])
# def criar_veiculo():
#     veiculo = flask.request.json
#     sw.veiculos.append(veiculo)
#     id = len(sw.veiculos) - 1
#     return flask.jsonify({"id":id})

# @app.route("/veiculos/<int:id>", methods=["PUT"])
# def modificar_veiculo(id):
#     veiculo = flask.request.json
#     sw.veiculos[id] = veiculo
#     return flask.jsonify({"ok": True})

