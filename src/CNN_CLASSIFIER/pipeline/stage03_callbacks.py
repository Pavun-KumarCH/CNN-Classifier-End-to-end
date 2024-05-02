from CNN_CLASSIFIER.config.configuration import ConfigurationManager
from CNN_CLASSIFIER.components import PrepareCallback
from CNN_CLASSIFIER import logger

class CallBacksPipeline:
    def main(self):
        config = ConfigurationManager()
        prepare_callback =  config.get_callbacks_config()
        prepare_callback = PrepareCallback(prepare_callback)
        callback_list = prepare_callback.get_tb_ckpt_callbacks()
            
        