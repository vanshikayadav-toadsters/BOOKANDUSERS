from datetime import datetime, timedelta
import uuid
import logging
import jwt
from passlib.context import CryptContext
from src.config import Config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(
    user_data: dict,
    expiry: timedelta = None,
    refresh: bool = False
) -> str:

    payload = {
        "user": user_data,
        "exp": datetime.utcnow() + (expiry if expiry else timedelta(minutes=60)),
        "jti": str(uuid.uuid4()),
        "refresh": refresh
    }

    token = jwt.encode(
        payload,
        Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> dict | None:
    try:
        token_data = jwt.decode(
            token,
            Config.JWT_SECRET,
            algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data

    except jwt.ExpiredSignatureError:
        logging.exception("Token expired")
        return None

    except jwt.InvalidTokenError:
        logging.exception("Invalid token")
        return None

    except Exception as e:
        logging.exception(e)
        return None
