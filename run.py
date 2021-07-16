import flask
import config.db
import sw.naves.blueprint as naves
import sw.personagens.blueprint as personagens
import sw.veiculos.blueprint as veiculos

app = flask.Flask(__name__)

app.register_blueprint(naves.bp)

app.register_blueprint(personagens.bp)

app.register_blueprint(veiculos.bp)

@app.route("/")
def home():
    return 'home'

if __name__ == "__main__":
    config.db.setup()
    app.run(debug=True)