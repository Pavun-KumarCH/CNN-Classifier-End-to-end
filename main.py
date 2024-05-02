from CNN_CLASSIFIER.pipeline.stage01_data_ingestion import DataIngestionTrainningPipeline
from CNN_CLASSIFIER.pipeline.stage02_base_model import BaseModelTrainningPipeline
from CNN_CLASSIFIER.pipeline.stage03_training import ModelTrainingPipeline
from CNN_CLASSIFIER.pipeline.stage04_evaluation import EvaluationPipeline

from CNN_CLASSIFIER import logger

Stage_name = "######### Data Ingestion Stage ###########"
try:
    logger.info(f">>>>>>>>>>> {Stage_name} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainningPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>> {Stage_name} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = "######### Model Building Stage ###########"
try:
    logger.info(f">>>>>>>>>>> {Stage_name} started <<<<<<<<<<")
    base_model = BaseModelTrainningPipeline()
    base_model.main()
    logger.info(f">>>>>>>>>>> {Stage_name} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = "######### Model Training Stage ###########"
try:
    logger.info(f"*******************************************")
    logger.info(f">>>>>>>>>>> {Stage_name} started <<<<<<<<<<")
    base_model = ModelTrainingPipeline()
    base_model.main()
    logger.info(f">>>>>>>>>>> {Stage_name} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = "######### Evaluation Stage ###########"
try:
    logger.info(f"*******************************************")
    logger.info(f">>>>>>>>>>> {Stage_name} started <<<<<<<<<<")
    base_model = EvaluationPipeline()
    base_model.main()
    logger.info(f">>>>>>>>>>> {Stage_name} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e