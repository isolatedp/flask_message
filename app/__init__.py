import importlib
import os

from flask import Flask

from app.configs import BaseConfig
from app.utils.inject_prepend import custom_url_for


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    # 自定義 Jinja2 模板 url_for
    app.jinja_env.globals['url_for'] = custom_url_for

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """
    註冊 Flask 擴展
    """
    from app.extensions import db
    db.init_app(app)


def register_blueprints(app):
    """
    註冊藍圖
    """
    bp_dir = os.path.join(app.root_path, 'blueprints')
    for dir_name in os.listdir(bp_dir):
        if not os.path.exists(os.path.join(bp_dir, dir_name, 'routers.py')):
            continue
        module = importlib.import_module(f'app.blueprints.{dir_name}.routers')
        app.register_blueprint(getattr(module, f'{dir_name}_bp'))
    