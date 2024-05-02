from CNN_CLASSIFIER.config.configuration import ConfigurationManager
from CNN_CLASSIFIER.components import BaseModel
from CNN_CLASSIFIER import logger

class BaseModelTrainningPipeline:
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_base_model_config()
        prepare_base_model = BaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
            
        