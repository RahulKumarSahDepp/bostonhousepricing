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

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template('index.html', prediction_text = "The predicted house price is {}".format(output))


if "__main__" == __name__:
    app.run(debug=True)



