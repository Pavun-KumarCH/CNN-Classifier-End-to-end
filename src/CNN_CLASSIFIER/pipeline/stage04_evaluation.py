from CNN_CLASSIFIER.config.configuration import ConfigurationManager
from CNN_CLASSIFIER.components import Evaluation
from CNN_CLASSIFIER import logger

class EvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evalaution = Evaluation(val_config)
        evalaution.evaluate()
        evalaution.save_score()
        