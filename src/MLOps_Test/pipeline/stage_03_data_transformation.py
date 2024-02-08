from MLOps_Test.config.configuration import ConfigurationManager
from MLOps_Test.components.data_transformation import DataTransformation
from MLOps_Test import logger

stage_name = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()

if __name__ == "__main__":
    try:
        logger.info(f"Stage {stage_name} started")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"Stage {stage_name} completed\n\n")
    except Exception as e:
        logger.error(e)
        raise e