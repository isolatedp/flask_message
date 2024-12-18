from flask import Blueprint

from .index.views import Index

main_bp = Blueprint("main", __name__, url_prefix="/")

main_bp.add_url_rule("/", view_func=Index.as_view("index"))