from flask import Flask,render_template,request,jsonify
import os
import numpy as np
import pandas as pd
from Customer_Segmentation.pipeline.prediction_pipeline import PredictionPipeline,CustomData
from Customer_Segmentation.exception.exception import customexception
import sys

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":
        try:
            data=CustomData(
                Age=int(request.form.get("Age")),
                Income=int(request.form.get("Income")),
                marital_status=str(request.form.get("marital_status")),
                Education=str(request.form.get("Education")),
                Occupation=str(request.form.get("Occupation")),
                Settlement=str(request.form.get("Settlement")),
                Sex=str(request.form.get("Sex"))
                )
            data=data.get_as_df()
            obj=PredictionPipeline()
            predict=obj.predict(data)
            maps={0:"Standard",1:"Platinum",2:"Gold",3:"Bronze"}
            res=maps[predict[0]]
            return render_template("results.html",prediction=res)
        except Exception as e:
            raise customexception(e,sys)

    else:
        return render_template('single.html')

# Other routes and functions...
if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080,debug=True)