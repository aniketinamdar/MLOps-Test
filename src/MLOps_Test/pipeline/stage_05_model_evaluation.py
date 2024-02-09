from MLOps_Test.config.configuration import ConfigurationManager
from MLOps_Test.components.model_evaluation import ModelEvaluation
from MLOps_Test import logger

stage_name = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f"Stage {stage_name} started")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"Stage {stage_name} completed\n\n")
    except Exception as e:
        logger.error(e)
        raise e