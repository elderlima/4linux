import flask as f
import dashboard

app = f.Flask(__name__)
app.secret_key = "rombado"

app.register_blueprint(dashboard.docker.blueprint.bp)
app.register_blueprint(dashboard.jenkins.blueprint.bp)

if __name__ == "__main__":
    app.run(debug=True)