from fastapi import APIRouter, Request
from routers.engine import engine
from models.data import AircraftData
from sqlalchemy import text, insert
import pandas as pd
import matplotlib.pyplot as plt
import base64
#cors

 


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


@router.get("/graph", tags=["data"])
def graph():
    try:
        with engine.begin() as conn:
            query = text("select * from aircraft_data")
            result = conn.execute(query)
            data = result.fetchall()
            df = pd.DataFrame(data)
            df["date"] = pd.to_datetime(df["date"])
            df["month"] = df["date"].dt.month
            df= df[df["time_to_failure"]==0]
            df[["month","time_to_failure"]].groupby("month").count().plot(title="Number of failures per month", kind="bar",xlabel="Month", ylabel="Number of failures",rot=0)
            plt.savefig("graph.png")
            with open("graph.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            return {"message": encoded_string.decode("utf-8")}
         
    except Exception as e:
        print(e)
        return {"message": str(e)}