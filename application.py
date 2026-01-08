import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException
import sys

application = Flask(__name__)
app = application


def validate_form_data(form_data):
    """Validate form inputs before processing"""
    errors = []
    
    # Check required fields
    required_fields = ['gender', 'ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
    for field in required_fields:
        if not form_data.get(field):
            errors.append(f"Missing required field: {field}")
    
    # Validate numeric fields
    try:
        reading_score = float(form_data.get('reading_score', 0))
        if not (0 <= reading_score <= 100):
            errors.append("Reading score must be between 0 and 100")
    except ValueError:
        errors.append("Reading score must be a valid number")
    
    try:
        writing_score = float(form_data.get('writing_score', 0))
        if not (0 <= writing_score <= 100):
            errors.append("Writing score must be between 0 and 100")
    except ValueError:
        errors.append("Writing score must be a valid number")
    
    return errors


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    # When the form is submitted it will be a POST request
    if request.method == 'POST':
        # Validate form data
        validation_errors = validate_form_data(request.form)
        if validation_errors:
            return render_template('home.html', errors=validation_errors), 400
        
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score')),
            )
            predict_df = data.get_data_as_data_frame()

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(predict_df)
            return render_template('home.html', results=results[0])
        except CustomException as e:
            return render_template('home.html', error=str(e.error_message)), 500
        except Exception as e:
            error_msg = f"An unexpected error occurred: {str(e)}"
            return render_template('home.html', error=error_msg), 500
    
    # For GET requests, show the form
    return render_template('home.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predictdata():
    # alias route kept for backward compatibility with older links
    return predict_datapoint()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('home.html', error="Page not found"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('home.html', error="Internal server error"), 500
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)