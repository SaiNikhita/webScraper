from flask import Flask, request, render_template, jsonify
import json
import numpy as np
from sklearn.externals import joblib
import pickle
#logre=joblib.load('jsonmodel.pkl')

ip=open("sri",'rb')
m=pickle.load(ip)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/Submit',methods=['POST'])
def Submit():
	if request.method == 'POST':
		print("hello")		
		data=request.form
		print(data)
		preg = int(request.form['Pregnancies'])
		gluc = float(request.form['Glucose'])
		bp = float(request.form['BloodPressure'])                
		st = float(request.form['SkinThickness'])                
		iss = float(request.form['Insulin'])                
		bmi=float(request.form['BMI'])                
		dpf=float(request.form['DiabetesPredigreeFunction'])                		
		age=int(request.form['Age'])
		k=[[preg,gluc,bp,st,iss,bmi,dpf,age]]                
		pred=m.predict(k)                
		return "prediction is"+str(pred)
		#return "hello"


if __name__ == '__main__':
  app.run(debug=True)
