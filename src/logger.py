import os
import sys
import logging
from datetime import datetime

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create logs directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create log file path
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(log_dir, log_file)

# File handler
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

# Stream handler for console output
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(stream_handler)

# Example log
if __name__ == "__main__":
    logging.info("Logging started")
