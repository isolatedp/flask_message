import traceback

def get_request_ip(request):
    try:
        ip = None
        x_forwarded_for = request.headers.get('X-Forwarded-For')
        if isinstance(x_forwarded_for, str):
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.remote_addr
        return ip

    except Exception as e:
        traceback.print_exc()