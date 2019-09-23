
# A very simple Flask Hello World app for you to get started with...
import numpy as np
from flask import Flask, request, jsonify
from sklearn.externals import joblib
#import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello I am Tunggal M. A. T.'

model = joblib.load(open('/home/tunggalmat/mysite/clf.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)
    output= []
    no = 1
    for data in datas :
        prediction = model.predict([np.array([data['EDUCATION'],data['SEX'],data['MARRIAGE'],data['PAY_1'],data['PAY_2'],data['PAY_3']])])
        if prediction == 0 :
            o = ('User '+str(no)+' Tidak Telat Bayar')
            output.append(o)
            no +=1
        else :
            o = ('User '+str(no)+' Telat Bayar')
            output.append(o)
            no +=1
    return jsonify(output)