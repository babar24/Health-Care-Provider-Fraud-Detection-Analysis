from flask import Flask, request, send_file, render_template
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

model = joblib.load('best_model.pkl')
std_data = joblib.load('standardized_data.pkl') 

classes = {0:'Not Fraud', 1:'Fraud'}

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/about')
def About():
    return render_template('home.html')

@app.route('/download')
def download_file():
    path = "TestDataTemplate.csv"
    return send_file(path, as_attachment = True)


@app.route('/', methods=['POST'])
def predict():
    
    Prv = request.form.get('provider')
    file_test=request.files.get('test')
    tst = pd.read_csv(file_test)
    x = tst.values
    x= std_data.transform(x)
    prediction = model.predict(x)

    return render_template("index.html", prediction = "The provider {} is {}".format(Prv, classes[prediction[0]]))

if __name__ == '__main__':
    app.run(debug = True)