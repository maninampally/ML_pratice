import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    # When the form is submitted it will be a POST request
    if request.method == 'POST':
        data = CustomData(
            gender=request.form.get('gender'),
            ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score') or 0),
            writing_score=float(request.form.get('writing_score') or 0),
        )
        predict_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(predict_df)
        return render_template('home.html', results=results)
    # For GET requests, show the form
    return render_template('home.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predictdata():
    # alias route kept for backward compatibility with older links
    return predict_datapoint()
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)