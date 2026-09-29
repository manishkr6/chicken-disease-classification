from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
  logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
  obj = DataIngestionTrainingPipeline()
  obj.main()
  logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n x65")
except Exception as e:
  logger.exception(e)
  raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
  logger.info(f"**************************************")
  logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
  obj = PrepareBaseModelTrainingPipeline()
  obj.main()
  logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
  logger.error(f"Error in stage {STAGE_NAME}: {e}")
  raise e