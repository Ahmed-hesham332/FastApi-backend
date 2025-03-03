import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Settings:
    POSTCODE: str = os.getenv("POSTCODE", "00000")  # Default if not set

settings = Settings()

# print(f"Loaded POSTCODE: {settings.POSTCODE}")  # Debug print
