from MLOps_Test.config.configuration import ConfigurationManager
from MLOps_Test.components.data_validation import DataValiadtion
from MLOps_Test import logger

stage_name = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f"Stage {stage_name} started")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"Stage {stage_name} completed\n\n")
    except Exception as e:
        logger.error(e)
        raise e