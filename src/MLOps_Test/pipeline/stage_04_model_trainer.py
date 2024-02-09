from MLOps_Test.config.configuration import ConfigurationManager
from MLOps_Test.components.model_trainer import ModelTrainer
from MLOps_Test import logger

stage_name = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
        logger.info(f"Stage {stage_name} started")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f"Stage {stage_name} completed\n\n")
    except Exception as e:
        logger.error(e)
        raise e