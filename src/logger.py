import logging
import os
from datetime import datetime

# Generate a timestamped log filename
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Create a "logs" directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Decide whether to log to file (local) or stdout (Render)
if os.environ.get("RENDER") == "true":
    # Render → log to stdout
    logging.basicConfig(
        level=logging.INFO,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    )
else:
    # Local dev → log to file
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    )

