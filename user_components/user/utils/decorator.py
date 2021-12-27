import jwt
from sanic import response
from functools import wraps
from entrypoint import settings

secret_key = settings.settings_factory().secret_key


def authorized():
    def decorator(f):
        @wraps(f)
        async def decorator_function(request, *args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"]
            if not token:
                return response.json({"message": "Token is missing"}, 401)
            try:
                data = jwt.decode(token, secret_key, algorithms="HS256")
                email = data["email"]
                if email:
                    responses = await f(request, *args, **kwargs)
                    return responses
                else:
                    return response.json({"message": "Please Login Again"}, 403)
            except Exception as e:
                return response.json({"message": f"{e}"}, 403)

        return decorator_function

    return decorator


def is_admin():
    def decorator(f):
        @wraps(f)
        async def decorator_function(request, *args, **kwargs):
            token = request.headers["Authorization"]
            data = jwt.decode(token, secret_key, algorithms="HS256")
            is_admin = data["is_admin"]
            if is_admin is True:
                responses = await f(request, *args, **kwargs)
                return responses
            else:
                return response.json({"error": "You do not have permission"}, 403)

        return decorator_function

    return decorator


def is_client():
    def decorator(f):
        @wraps(f)
        async def decorator_function(request, *args, **kwargs):
            token = request.headers["Authorization"]
            data = jwt.decode(token, secret_key, algorithms="HS256")
            is_client = data["is_client"]
            if is_client is True:
                responses = await f(request, *args, **kwargs)
                return responses
            else:
                return response.json({"error": "You do not have permission"}, 403)

        return decorator_function

    return decorator
