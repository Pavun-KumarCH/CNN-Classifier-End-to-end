import os
from pathlib import Path
from CNN_CLASSIFIER.constants import *
from CNN_CLASSIFIER.utils import read_yaml, create_directories
from CNN_CLASSIFIER.entity import (DataIngestionConfig,
                                   BaseModelConfig,
                                   CallbackConfig,
                                   TrainingConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model

        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES,
        )
        return base_model_config
    
    def get_callbacks_config(self) -> CallbackConfig:
        config = self.config.callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorflow_root_log_dir)
        ])

        callback_config = CallbackConfig(
            root_dir = Path(config.root_dir),
            tensorflow_root_log_dir = Path(config.tensorflow_root_log_dir),
            checkpoint_model_filepath = Path(config.checkpoint_model_filepath)
        )
        return callback_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "PetImages")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        return training_config