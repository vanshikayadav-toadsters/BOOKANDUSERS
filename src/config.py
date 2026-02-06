import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key-here")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    DATABASE_URL = os.getenv("DATABASE_URL")
    REFRESH_TOKEN_EXPIRY = int(os.getenv("REFRESH_TOKEN_EXPIRY", "7"))

# For backward compatibility
JWT_SECRET = Config.JWT_SECRET
JWT_ALGORITHM = Config.JWT_ALGORITHM
DATABASE_URL = Config.DATABASE_URL
