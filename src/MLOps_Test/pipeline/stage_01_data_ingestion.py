from MLOps_Test.config.configuration import ConfigurationManager
from MLOps_Test.components.data_ingestion import DataIngestion
from MLOps_Test import logger

stage_name = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f"Stage {stage_name} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Stage {stage_name} completed\n\n")
    except Exception as e:
        logger.error(e)
        raise e