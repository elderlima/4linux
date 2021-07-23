import flask as f
import dashboard
import config.logs as l

app = f.Flask(__name__)
app.secret_key = "rombado"


for handler in (l.stdout_handler, l.file_handler, l.sock_handler):
    app.logger.addHandler(handler)

app.register_blueprint(dashboard.docker.blueprint.bp)
app.register_blueprint(dashboard.jenkins.blueprint.bp)

if __name__ == "__main__":
    app.run(debug=True)