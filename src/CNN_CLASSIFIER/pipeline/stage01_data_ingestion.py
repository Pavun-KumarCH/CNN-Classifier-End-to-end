from CNN_CLASSIFIER.config.configuration import ConfigurationManager
from CNN_CLASSIFIER.components import DataIngestion
from CNN_CLASSIFIER import logger

class DataIngestionTrainningPipeline:
    def main(self):
        config = ConfigurationManager()
        data_ingestion = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
        
        