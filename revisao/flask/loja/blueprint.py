import flask as f
from config.api import mkbsonresponse
from . import models

bp = f.Blueprint("loja", __name__, url_prefix="/loja")

@bp.route("")
def list_produtos():
    produtos = models.list_produtos()
    return mkbsonresponse(produtos)

@bp.route("/<id>")
def get_produtos(id):
    return mkbsonresponse(models.get_produtos(id))

