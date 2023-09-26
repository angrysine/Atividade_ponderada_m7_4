# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import matplotlib.pyplot as plt
import base64

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("teste_api")

# Create input/output pydantic models
class input_model(BaseModel):
    CustomerID: int
    Gender: int
    Age: int
    Income: int



@app.get("/")
def home():
    return "API is working!"

# Define predict function
@app.post("/predict")
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}

@app.get("/plot")
def plot_image(lower_bound:int,upper_bound:int):
    df = pd.read_csv('./archive/Mall_Customers.csv')
    reduced_df = df[['Age','Spending Score (1-100)']].groupby('Age').mean().reset_index()
    del df
    upper_bound_age = upper_bound
    lower_bound_age = lower_bound
    mask = (reduced_df['Age'] <= upper_bound_age) & (reduced_df['Age'] >= lower_bound_age)
    reduced_df = reduced_df[mask]
    reduced_df.plot(x="Age",y="Spending Score (1-100)",kind='bar',figsize=(20,10),title="spending score per age")
    plt.xticks(rotation=0, ha='right')
    plt.savefig('./images/income_per_age.png')
    del reduced_df
    with open("./images/income_per_age.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
