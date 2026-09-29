from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chicken_disease_classification.pipeline.stage_03_training import ModelTrainingPipeline
from chicken_disease_classification.pipeline.stage_04_evaluation import EvaluationPipeline

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


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Evaluation stage"
try:
  logger.info(f"*******************")
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  model_evalution = EvaluationPipeline()
  model_evalution.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
      logger.exception(e)
      raise e