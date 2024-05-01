from CNN_CLASSIFIER.pipeline.stage01_data_ingestion import DataIngestionTrainningPipeline
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
