import logging
import os
from datetime import datetime

# Generate a log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full log file path inside 'logs/' directory
logs_path = os.path.join(os.getcwd(), "logs")
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Ensure 'logs/' folder exists
os.makedirs(logs_path, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# # Test log
# if __name__ == "__main__":
#     logging.info("Logging has stArted ")
