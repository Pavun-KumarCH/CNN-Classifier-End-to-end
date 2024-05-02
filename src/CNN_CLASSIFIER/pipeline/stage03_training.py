from CNN_CLASSIFIER.config.configuration import ConfigurationManager
from CNN_CLASSIFIER.components import Training,PrepareCallback
from CNN_CLASSIFIER import logger

class ModelTrainingPipeline:
    def main(self):
        # Callbacks
        config = ConfigurationManager() 
        prepare_callback =  config.get_callbacks_config()
        prepare_callback = PrepareCallback(prepare_callback)
        callback_list = prepare_callback.get_tb_ckpt_callbacks()
        
        # Training
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.training_valid_generation()
        training.train(
        callback_list = callback_list)
            
        