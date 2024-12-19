# 提供靜態資源前置載入的機制
import os

from flask import url_for
from dotenv import load_dotenv


load_dotenv()

def inject_prepend():
    nginx_prepend = os.environ.get("NGINX_PREPEND", "")
    if nginx_prepend:
        return lambda x: f"/{nginx_prepend}" + x
    return lambda x: x


def custom_url_for(endpoint, **values):
    url = url_for(endpoint, **values)
    prepend_func = inject_prepend()
    return prepend_func(url)
