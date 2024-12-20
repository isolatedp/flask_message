# 提供靜態資源前置載入的機制
import os

from flask.helpers import url_for
from dotenv import load_dotenv


load_dotenv()

def inject_prepend():
    """
    搭配環境變數 NGINX_PREPEND 來注入前置路徑
    """
    nginx_prepend = os.environ.get("NGINX_PREPEND", "")
    if nginx_prepend:
        return lambda x: f"/{nginx_prepend}" + x
    return lambda x: x


def custom_url_for(endpoint, **values):
    """
    自定義 url_for
    """
    url = url_for(endpoint, **values)
    prepend_func = inject_prepend()
    return prepend_func(url)
