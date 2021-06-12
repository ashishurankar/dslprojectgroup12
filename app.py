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
app = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))
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
        prediction=model.predict([PRODUCT,SUB_PRODUCT,ISSUE,
                                  COMPANY,STATE,SUBMITTED_VIA,COMPANY_RESPONSE_TO_CONSUMER,DATE_DIFF])
        output = prediction
        return render_template('index.html',prediction_text="Will Timely response be provided?: {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)