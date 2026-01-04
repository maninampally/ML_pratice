import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging


class TrainingPipeline:
    def __init__(self):
        pass

    def initiate_train_pipeline(self):
        try:
            logging.info(">>>>> Started the training pipeline")
            
            # Step 1: Data Ingestion
            logging.info("Starting data ingestion...")
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed. Train: {train_data_path}, Test: {test_data_path}")

            # Step 2: Data Transformation
            logging.info("Starting data transformation...")
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
                train_data_path, test_data_path
            )
            logging.info(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")

            # Step 3: Model Training
            logging.info("Starting model training...")
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Model training completed. R² Score: {r2_score}")

            logging.info(">>>>> Training pipeline completed successfully!")
            
            return r2_score

        except Exception as e:
            logging.error("Error occurred during training pipeline")
            raise CustomException(e, sys)


if __name__ == "__main__":
    pipeline = TrainingPipeline()
    r2_score = pipeline.initiate_train_pipeline()
    print(f"\n{'='*50}")
    print(f"FINAL R² SCORE: {r2_score:.4f}")
    print(f"{'='*50}\n")
