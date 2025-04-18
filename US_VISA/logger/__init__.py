## Custom Logging
import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = "log"
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Ensure the log directory exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(logs_path)
        formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


