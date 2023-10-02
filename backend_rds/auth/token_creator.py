import jwt
from datetime import datetime, timedelta
import secrets


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    secret = secrets.token_urlsafe(32)
    encoded_jwt = jwt.encode(to_encode, secret, algorithm="HS256")
    return encoded_jwt, secret


def verify_delta(decoded_jwt, delta: timedelta = timedelta(minutes=60)):
    if datetime.utcnow() > datetime.fromtimestamp(decoded_jwt["exp"]):
        raise Exception("Token expired")
    else:
        return True


def decode_access_token(token: str, secret: str):
    try:
        decoded_jwt = jwt.decode(
            token, secret, algorithms=["HS256"])

    except Exception as e:
        print(e)
        raise e
    try:
        verify_delta(decoded_jwt)
    except Exception as e:
        if str(e) == "Token expired":
            print("token expired")
            raise e
    return "valid token"
