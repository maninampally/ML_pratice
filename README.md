# Student Performance Prediction System

A machine learning web application that predicts student math performance based on various demographic and academic features.

## Overview

This project uses multiple regression models (Random Forest, XGBoost, Gradient Boosting, etc.) to predict student math scores. The best performing model is deployed as a Flask web application with a user-friendly interface.

## Features

- **Data Processing Pipeline**: Automated data ingestion, transformation, and preprocessing
- **Model Training**: Comparison of 6 different regression models with hyperparameter tuning
- **Web Interface**: Interactive Flask application for making predictions
- **Containerization**: Docker support for easy deployment
- **CI/CD Pipeline**: Automated deployment to Azure Web Apps via GitHub Actions
- **Logging & Error Handling**: Comprehensive logging and custom exception handling
- **Modular Architecture**: Clean separation of concerns with components, pipelines, and utilities

## Tech Stack

- **Framework**: Flask
- **ML Libraries**: scikit-learn, XGBoost, CatBoost
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Deployment**: Docker, Azure Web Apps
- **CI/CD**: GitHub Actions

## Project Structure

```
ML_pratice/
├── application.py          
├── setup.py                
├── requirements.txt        
├── Dockerfile              
├── artifacts/              
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
├── src/
│   ├── components/         
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/           
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py        
│   ├── logger.py           
│   └── utils.py            
├── templates/              
│   ├── index.html
│   └── home.html
├── notebook/               
└── .github/workflows/      
```

## Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ML_pratice
   ```

2. **Create virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python application.py
   ```
   
   The app will be available at `http://0.0.0.0:5000`

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t student-performance:latest .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 student-performance:latest
   ```

## Usage

### Making Predictions

1. Open the web application in your browser
2. Fill in the student information:
   - Gender
   - Ethnicity
   - Parental Level of Education
   - Lunch Type
   - Test Preparation Course
   - Reading Score
   - Writing Score
3. Click "Predict" to get the predicted math score

### Training a New Model

```python
from src.pipeline.train_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.initiate_training()
```

## Model Performance

The project evaluates the following models:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- AdaBoost Regressor

Each model is tuned using GridSearchCV to find optimal hyperparameters.

## Input Features

| Feature | Type | Description |
|---------|------|-------------|
| gender | categorical | Student's gender (male/female) |
| ethnicity | categorical | Student's ethnic group |
| parental_level_of_education | categorical | Parent's education level |
| lunch | categorical | Lunch type (standard/free-reduced) |
| test_preparation_course | categorical | Test prep status (none/complete) |
| reading_score | numerical | Student's reading score (0-100) |
| writing_score | numerical | Student's writing score (0-100) |

## Output

- **Prediction**: Predicted math score (numerical value)

## Logging

Application logs are stored in the `logs/` directory with timestamp-based filenames. Logs include:
- Data ingestion steps
- Model training progress
- Prediction requests
- Errors and exceptions

## Error Handling

The application uses custom exception handling to provide detailed error messages including:
- File name where error occurred
- Line number
- Error description

## Deployment

The project includes a GitHub Actions workflow for automated deployment to Azure Web Apps:

```yaml
- Triggered on push to main branch
- Builds and tests the application
- Deploys to Azure Web Apps (studentssperformance3)
```

**Requirements for Azure deployment:**
- Azure subscription
- Web App created in Azure
- Publish profile added as GitHub secret: `AZUREAPPSERVICE_PUBLISHPROFILE_*`

## Configuration

### Environment Variables
- `FLASK_APP`: application.py
- `FLASK_ENV`: production (default)

### Model Paths
- Trained Model: `artifacts/model.pkl`
- Preprocessor: `artifacts/preprocessor.pkl`

## Troubleshooting

**Issue**: Model file not found
- **Solution**: Ensure you've trained the model first using the training pipeline

**Issue**: Input validation error
- **Solution**: Verify all form fields are filled with valid values. Reading and writing scores should be between 0-100

**Issue**: Docker build fails
- **Solution**: Ensure Python 3.10+ is available and all dependencies in requirements.txt are compatible

## Future Enhancements

- [ ] Add unit tests and integration tests
- [ ] Implement model versioning and A/B testing
- [ ] Add data validation on frontend
- [ ] Implement log rotation for long-running applications
- [ ] Add API documentation (Swagger/OpenAPI)
- [ ] Support for batch predictions via CSV upload
- [ ] Model explainability (SHAP values)

## License

This project is part of an ML learning initiative.

## Author

Manikantha Nampally