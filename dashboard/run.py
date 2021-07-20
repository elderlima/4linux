import flask as f
import dashboard

app = f.Flask(__name__)

app.register_blueprint(dashboard.docker.blueprint.bp)

if __name__ == "__main__":
    app.run(debug=True)