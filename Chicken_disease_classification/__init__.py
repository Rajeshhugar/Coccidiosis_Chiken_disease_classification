import os 
import sys
import logging
import datetime

logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"running_logs_{current_time}.log"
log_filepath = os.path.join(log_dir, log_filename)

logging.basicConfig(level=logging.INFO, format=logging_str, handlers=[
    logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)
])

logger = logging.getLogger('Chicken_disease_classification')


