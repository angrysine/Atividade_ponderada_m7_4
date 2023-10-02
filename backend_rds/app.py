from fastapi import FastAPI
import os 
import uvicorn
from dotenv import load_dotenv
import os
from routers.data import router as data_router
from routers.user import router as user_router

load_dotenv("./.env")

host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("database")
user = os.getenv("user")
password = os.getenv("password")
print("host: ", host, "port: ", port, "database: ", database, "user: ", user, "password: ", password)


app = FastAPI()
app.include_router(data_router)
app.include_router(user_router)




conf ={
    'host':host,
    'port':port,
    'database':database,
    'user':user,
    'password': password
}




if __name__ == '__main__':
    uvicorn.run(app)