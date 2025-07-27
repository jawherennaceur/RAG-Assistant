
import logging
import os

from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    logger.error("Missing GOOGLE_API_KEY in environment")
    raise RuntimeError("GOOGLE_API_KEY is required")


HuggingFace_KEY = os.getenv("HuggingFace_KEY")
if not HuggingFace_KEY:
    logger.error("Missing HuggingFace_KEY in environment")
    raise RuntimeError("HuggingFace_KEY is required")


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
