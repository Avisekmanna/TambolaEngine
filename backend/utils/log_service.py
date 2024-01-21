
from loguru import logger
import os
from datetime import datetime

logs_directory = 'logs'
log_file_path = os.path.join(logs_directory, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Ensure logs directory exists
os.makedirs(logs_directory, exist_ok=True)

logger.add(log_file_path, rotation='1 day', level='INFO', colorize=True)

def get_logger():
    return logger
