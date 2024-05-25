from flask import Flask,request,render_template
import numpy as np
import sklearn
import pandas
import pickle
import warnings as w 
w.filterwarnings("ignore")


# importing model
model = pickle.load(open('RandomForest.pkl','rb'))

# creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def prediction():
    N = int(request.form.get('N'))
    P = int(request.form.get('P'))
    K = int(request.form.get('K'))
    temperature = float(request.form.get('temperature'))
    humidity = float(request.form.get('humidity'))
    ph = float(request.form.get('ph'))
    rainfall = float(request.form.get('rainfall'))


    result = model.predict(np.array([[N,P,K,temperature,humidity,ph,rainfall]]))



    if True:
        pred = "{} is a best crop to be cultivated. ".format(result)
        return render_template('index.html',result = pred)


# # python main
if __name__ == "__main__":
    app.run(debug=True)