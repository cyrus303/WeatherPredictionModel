from flask import Flask,render_template,request,jsonify
#from source import inpo,clear
import subprocess
import os, sys
from subprocess import check_output
import time
import json
from flask import request, redirect
import TempPrediction
import csv
import numpy as np

application= Flask(__name__)
#model = pickle.load(open('TempPrediction.pkl', 'rb'))

@application.route('/')
def index():
    return render_template('display.html')

@application.route('/predict', methods=['POST'])
def predict():
    int_features =request.form['interview_score']

    with open(r'C:/Users/Reddy/Desktop/PROJECT/flas/mout.csv','rt') as f:
        reader = csv.reader(f)
        #print("4444444444444444444444444444444444")
        for row in reader:
            if row[0] == int_features:
                output = row[1]
                output=float(output)
                output = round(output, 2)

                return render_template('display.html', output= output)
@application.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = TempPrediction.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

@application.route('/indbig')
def indbig():
    return render_template('weather.html')


@application.route('/convertor')
def convertor():
    return render_template('display.html')


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    application.run(host="0.0.0.0")
