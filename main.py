from Chicken_disease_classification import logger
from Chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Chicken_disease_classification.pipeline.stage_03_training import ModelTrainingPipeline
from Chicken_disease_classification.pipeline.stage_04_evaluation import ModelEvaluationPipeline



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>stage{STAGE_NAME} started<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} completed  <<<<\n\nx===========x")
    
except Exception as e:
    logger.exception()
    raise e     


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>stage{STAGE_NAME} started<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} completed  <<<<\n\nx===========x")
    
except Exception as e:
    logger.exception()
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
    
STAGE_NAME = "Evaluation stage "
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = ModelEvaluationPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    