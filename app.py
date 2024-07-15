from flask import Flask,request,render_template
import pickle
import numpy as np
import pandas as pd
import os
app=Flask(__name__)
encoders_path = os.path.dirname(os.path.abspath(__file__))
model=pickle.load(open(os.path.join(encoders_path, 'temperature.pkl'),'rb'))

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    co2=float(request.form['CO2_room'])
    humidity=float(request.form['Relative_humidity_room'])
    lighting=float(request.form['Lighting_room'])
    rain=float(request.form['Meteo_Rain'])
    wind=float(request.form['Meteo_Wind'])
    sunlight=float(request.form['Meteo_Sun_light_in_west_facade'])
    outdoor_humidity=float(request.form['Outdoor_relative_humidity_Sensor'])
    pred=[[co2,humidity,lighting,rain,wind,sunlight,outdoor_humidity]]
    print(pred)
    output=model.predict(pred)
    print(output)
    return render_template('predict.html',prediction_text=output)

if __name__ == '__main__':
    app.run(debug=True)