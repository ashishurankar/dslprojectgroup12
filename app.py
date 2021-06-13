# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:55:15 2021

@author: admin
"""

from flask import Flask, render_template, request
import gunicorn
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import statistics as st
app = Flask(__name__, template_folder='template')
model1 = pickle.load(open('data0model.pkl', 'rb'))
model2 = pickle.load(open('data1model.pkl', 'rb'))
model3 = pickle.load(open('data2model.pkl', 'rb'))
model4 = pickle.load(open('data3model.pkl', 'rb'))
model5 = pickle.load(open('data4model.pkl', 'rb'))
model6 = pickle.load(open('data5model.pkl', 'rb'))
model7 = pickle.load(open('data6model.pkl', 'rb'))
model8 = pickle.load(open('data7model.pkl', 'rb'))
model9 = pickle.load(open('data8model.pkl', 'rb'))
model10 = pickle.load(open('data9model.pkl', 'rb'))
model11 = pickle.load(open('data10model.pkl', 'rb'))
model12 = pickle.load(open('data11model.pkl', 'rb'))
model13 = pickle.load(open('data12model.pkl', 'rb'))
model14 = pickle.load(open('data13model.pkl', 'rb'))
model15 = pickle.load(open('data14model.pkl', 'rb'))
model16 = pickle.load(open('data15model.pkl', 'rb'))
model17 = pickle.load(open('data16model.pkl', 'rb'))
model18 = pickle.load(open('data17model.pkl', 'rb'))
model19 = pickle.load(open('data18model.pkl', 'rb'))
model20 = pickle.load(open('data19model.pkl', 'rb'))
model21 = pickle.load(open('data20model.pkl', 'rb'))
model22 = pickle.load(open('data21model.pkl', 'rb'))
model23 = pickle.load(open('data22model.pkl', 'rb'))
model24 = pickle.load(open('data23model.pkl', 'rb'))
model25 = pickle.load(open('data24model.pkl', 'rb'))
model26 = pickle.load(open('data25model.pkl', 'rb'))
model27 = pickle.load(open('data26model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        PRODUCT = str(request.form['PRODUCT'])
        SUB_PRODUCT = str(request.form['SUB_PRODUCT'])
        ISSUE = str(request.form['ISSUE'])
        COMPANY = str(request.form['COMPANY'])
        STATE = str(request.form['STATE'])
        SUBMITTED_VIA = str(request.form['SUBMITTED_VIA'])
        COMPANY_RESPONSE_TO_CONSUMER = str(request.form['COMPANY_RESPONSE_TO_CONSUMER'])
        DATE_DIFF = int(request.form['DATE_DIFF'])
        def ans(my_models):
            my_prediction=my_models.predict([PRODUCT,SUB_PRODUCT,ISSUE,
                                  COMPANY,STATE,SUBMITTED_VIA,COMPANY_RESPONSE_TO_CONSUMER,DATE_DIFF])
            return my_prediction
        prediction = st.mode([ans(model1),ans(model2),ans(model3),ans(model4),ans(model5),ans(model6),ans(model7),
                      ans(model8),ans(model9),ans(model9),ans(model11),ans(model12),ans(model13),ans(model14),
                      ans(model15),ans(model16),ans(model17),ans(model18),ans(model19),ans(model20),ans(model21),
                      ans(model22),ans(model23),ans(model24),ans(model25),ans(model26),ans(model27)])
        output = prediction
        return render_template('index.html',prediction_text="Will Timely response be provided?: {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)