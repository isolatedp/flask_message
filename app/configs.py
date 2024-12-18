import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
import yaml

load_dotenv()

app_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(app_dir)
settings_dir = os.path.join(project_dir, "settings")

app_env = os.environ.get("APP_ENV", "PROD")
settings_filename = f"settings_prod.yaml"
settings = None
if app_env == "LOCAL":
    settings_filename = "settings_local.yaml"
elif app_env == "DEV":
    settings_filename = "settings_dev.yaml"

with open(os.path.join(settings_dir, settings_filename), "r") as f:
    settings = yaml.safe_load(f)

database_info = settings["database"]

class BaseConfig:
    # Flask Settings
    SECRET_KEY = os.environ.get("SECRET_KEY", "kevinDev")

    # Database Settings
    url = ''
    if database_info and len(database_info.keys()) == 1:
        db_name = list(database_info.keys())[0]
        prefix = 'mysql+pymysql://'
        host = database_info[db_name]['host']
        port = database_info[db_name]['port']
        user = database_info[db_name]['user']
        pwd = quote_plus(database_info[db_name]['password'])
        db = database_info[db_name]['name']
        url = f"{prefix}{user}:{pwd}@{host}:{port}/{db}"
    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True
        , 'pool_recycle': 1800
    }
        