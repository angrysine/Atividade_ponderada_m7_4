from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv("./.env")

host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("database")
user = os.getenv("user")
password = os.getenv("password")
print("host: ", host, "port: ", port, "database: ", database, "user: ", user, "password: ", password)

conf ={
    'host':host,
    'port':port,
    'database':database,
    'user':user,
    'password': password
}
# engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
engine = create_engine("sqlite:///data.db")
