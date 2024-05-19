from KidneyDiseaseClassifier import logger
from KidneyDiseaseClassifier.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from KidneyDiseaseClassifier.pipeline.stage2_prepare_base_model import PrepareBaseModelTrainingPipeline
from KidneyDiseaseClassifier.pipeline.stage3_model_training import ModelTrainingPipeline
from KidneyDiseaseClassifier.pipeline.stage4_model_evaluation import ModelEvaluationPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
    
except Exception as e:
    logger.exception(e)





STAGE_NAME = "Base Model Preparation Stage"

try:
    logger.info("*"*10)
    logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Training"

try:
    logger.info("*"*10)
    logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
    
except Exception as e:
    logger.exception(e)