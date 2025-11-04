import pickle
from flask import Flask, request, app, jsonify, render_template, redirect
import numpy as np
import pandas as pd

app = Flask(__name__)

regmodel = pickle.load(open("model.pkl", 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)
    print(output)
    return jsonify(output[0])

if "__main__" == __name__:
    app.run(debug=True)



