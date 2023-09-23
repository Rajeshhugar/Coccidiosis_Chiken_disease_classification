from Chicken_disease_classification.config.configuration import ConfigurationManager

from Chicken_disease_classification.components.evaluation import Evaluation
from Chicken_disease_classification import logger




STAGE_NAME = "Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()