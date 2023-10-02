from models.data import AircraftData
from sqlalchemy import create_engine
from models.base import Base
from models.user import User
from app import conf

print(conf)

if __name__ == '__main__':
    engine = create_engine("sqlite:///data.db")

    # engine = create_engine("postgresql://{user}:{password}@{host}:{port}/{database}".format(**conf))
    Base.metadata.create_all(engine)
