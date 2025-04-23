from fastapi import HTTPException, status, Depends

from backend.config import get_settings
from fastapi.security import OAuth2PasswordBearer

from enum import IntEnum
from dataclasses import dataclass

from datetime import datetime, timedelta

from jose import jwt, JWTError

settings = get_settings()

SECRET_KEY = settings.jwt_secret
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

class Role(IntEnum):
    NOT_USER = 0
    USER_NOT_AUTH = 1
    USER_AUTH = 2
    ADMIN = 3

@dataclass
class CurrentUser:
    user_id: str
    role: Role


def create_access_token(payload: dict,
                        role: Role,
                        expires_delta: timedelta = timedelta(hours=6)):
    expire = datetime.now() + expires_delta
    payload.update({'exp': expire, 'role': role})
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_current_user(token: str = Depends(oauth2_scheme)) -> CurrentUser:
    payload = decode_access_token(token)
    user_id = payload.get('user_id')
    role = payload.get('role')
    if not user_id or not role or role == Role.NOT_USER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return CurrentUser(user_id, Role(role))

