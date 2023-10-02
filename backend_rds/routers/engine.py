from sqlalchemy import create_engine
# engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
engine = create_engine("sqlite:///data.db")
