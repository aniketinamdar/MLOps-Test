from MLOps_Test import logger
from MLOps_Test.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLOps_Test.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLOps_Test.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MLOps_Test.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from MLOps_Test.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


stage_name = "Data Ingestion Stage"

try:
    logger.info(f"Stage {stage_name} started\n")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Stage {stage_name} completed\n\n")
except Exception as e:
    logger.error(e)
    raise e


stage_name = "Data Validation Stage"

try:
    logger.info(f"Stage {stage_name} started\n")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Stage {stage_name} completed\n\n")
except Exception as e:
    logger.error(e)
    raise e


stage_name = "Data Transformation Stage"

try:
    logger.info(f"Stage {stage_name} started\n")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Stage {stage_name} completed\n\n")
except Exception as e:
    logger.error(e)
    raise e

stage_name = "Model Trainer Stage"

try:
    logger.info(f"Stage {stage_name} started")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"Stage {stage_name} completed\n\n")
except Exception as e:
    logger.error(e)
    raise e

stage_name = "Model Evaluation Stage"

try:
    logger.info(f"Stage {stage_name} started")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"Stage {stage_name} completed\n\n")
except Exception as e:
    logger.error(e)
    raise e