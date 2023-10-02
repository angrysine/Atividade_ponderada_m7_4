from fastapi import APIRouter, Request
from routers.engine import engine
from models.data import AircraftData
from sqlalchemy import text, insert
import pandas as pd

router = APIRouter()


@router.post("/add_data", tags=["data"])
async def add_data(request: Request):
    try:
        json_list = await request.json()
        parquet_list = json_list["data"]

        with engine.begin() as conn:

            conn.execute(insert(AircraftData), parquet_list)

        return {"message": "Data added successfully"}
    except Exception as e:
        print(e)
        return {"message": str(e)}


@router.get("/get_data", tags=["data"])
async def get_data():
    try:
        with engine.begin() as conn:
            query = text("select * from aircraft_data")
            result = conn.execute(query)
            data = result.fetchall()
            df = pd.DataFrame(data)
            df.columns = result.keys()
            return df.to_dict(orient="records")
    except Exception as e:
        print(e)
        return {"message": str(e)}
