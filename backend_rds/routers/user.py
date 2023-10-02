from fastapi import APIRouter, Request
from models.user import User
from sqlalchemy import select, insert, update
from routers.engine import engine
from auth.token_creator import create_access_token, decode_access_token
import bcrypt
router = APIRouter()


# id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String)
#     password = Column(String)
#     date = Column(String)
#     user_secret = Column(String)

@router.post("/add_user", tags=["user"])
async def create_user(request: Request):
    try:
        data = await request.json()
        salt = bcrypt.gensalt()

        with engine.begin() as conn:
            conn.execute(insert(User), {"username": data["username"], "password": bcrypt.hashpw(
                data["password"].encode("utf-8"), salt), "date": "", "user_secret": ""})
        return {"message": "user created"}

    except Exception as e:
        print(e)
        return {"message": str(e)}


@router.post("/login", tags=["user"])
async def login(request: Request):
    try:
        data = await request.json()
        with engine.begin() as conn:
            password = data["password"]
            username = data["username"]
            stm = select(User).where(User.username == username)
            result = conn.execute(stm).fetchone()

            if bcrypt.checkpw(password.encode("utf-8"), result.password):
                token, secret = create_access_token(
                    {"username": username, "password": password})
                stm = update(User).where(User.username ==
                                         username).values(user_secret=secret)
                conn.execute(stm)
                return {"token": token}
            else:
                raise Exception("Invalid user or password")
    except Exception as e:
        return {"error": str(e)}


@router.post("/validate_token", tags=["user"])
async def validate(request: Request):
    data = await request.json()
    token = data["token"]
    user = data["username"]
    with engine.begin() as conn:
        try:
            stm = select(User).where(User.username == user)
            result = conn.execute(stm).fetchone()
            secret = result.user_secret
        except Exception as e:
            return {"message": str(e)}
        try:
            message = decode_access_token(token, secret)
            return {"message": message}
        except Exception as e:
            return {"message": str(e)}
