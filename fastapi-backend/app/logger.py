from loguru import logger
import sys

# Configure logging
logger.remove()  # Remove default logger
logger.add(sys.stdout, format="{time} | {level} | {message}", level="INFO")

logger.add("logs/app.log", rotation="1 day", level="INFO")  # Log to a file
