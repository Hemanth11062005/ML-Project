import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Log directory structure: logs/YYYY-MM-DD/log_file.log
current_date = datetime.now().strftime('%Y-%m-%d')
logs_path = os.path.join(os.getcwd(), "logs", current_date)
os.makedirs(logs_path, exist_ok=True)

# Log file path
LOG_FILE = f"{datetime.now().strftime('%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Log configuration with rotation
handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5 * 1024 * 1024, backupCount=5)  # 5 MB max per file, 5 backups
logging.basicConfig(
    handlers=[handler],
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG  # Change to logging.INFO for production
)
