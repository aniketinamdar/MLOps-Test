from MLOps_Test import logger
from MLOps_Test.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

stage_name = "Data Ingestion Stage"

try:
    logger.info(f"Stage {stage_name} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Stage {stage_name} completed\n\n")
except Exception as e:
    logger.error(e)
    raise e
