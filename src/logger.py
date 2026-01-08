import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create rotating file handler (max 10MB per file, keep last 5 files)
file_handler = RotatingFileHandler(
    LOG_FILE_PATH,
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=5
)

# Create formatter
formatter = logging.Formatter(
    "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

# Add formatter to handler
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)

# Also add console handler for debugging
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Configure the basic logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("Logger has been set up with rotation enabled.")
