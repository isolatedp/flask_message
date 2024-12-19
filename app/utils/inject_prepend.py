# 提供靜態資源前置載入的機制
import os
from dotenv import load_dotenv

load_dotenv()

def inject_prepend():
    nginx_prepend = os.environ.get("NGINX_PREPEND", "")
    if nginx_prepend:
        return lambda x: f"/{nginx_prepend}" + x
    return lambda x: x
