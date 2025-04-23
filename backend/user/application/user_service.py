from dependency_injector.wiring import inject
from fastapi import HTTPException, status
from jose import jwt
from ulid import ULID
from backend.user.domain.repository.user_repository import IUserRepository
from backend.user.domain.user import User as UserVo
from backend.utils.crypto import Crypto
from datetime import datetime
from backend.user.interface.controller import UpdateUserBody, CreateUserBody
from backend.utils import props
from backend.common.auth import Role, create_access_token
import ujson as json

class UserService:
    @inject
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
        self.ulid = ULID()
        self.crypto = Crypto()

    def get_user_service(self):
        return UserService()

    def create_user(self, user_body: CreateUserBody) -> UserVo:
        _user = None
        try:
            _user = self.user_repository.find_by_user_id(user_body.user_id)
        except HTTPException as e:
            if e.status_code != 422:
                raise e

        if _user:
            raise HTTPException(status_code=400, detail="User already exists")

        now = datetime.now()
        user: UserVo = UserVo(**props(user_body), id=0, joined_at=now, last_login_time=now)
        user.role = Role.USER_NOT_AUTH
        user.password = self.crypto.encrypt(user.password)

        self.user_repository.save(user)
        return user

    def get_users(self, page: int, per_page: int) -> tuple[int, list[UserVo]]:
        return self.user_repository.get_users(page, per_page)

    def update_user(self, user_id, user_body: UpdateUserBody) -> UserVo:
        user = None
        try:
            user: UserVo = self.user_repository.find_by_user_id(user_id)

        except HTTPException as e:
            if e.status_code == 422:
                raise HTTPException(status_code=422, detail="User does not exist")

        body = user_body.model_dump(exclude_none=True)
        for k, v in body.items():
            setattr(user, k, v)

        user.updated_at = datetime.now()
        self.user_repository.update(user)
        return user

    def login(self, user_id: str, password: str) -> dict:
        user = None
        try:
            user = self.user_repository.find_by_user_id(user_id)
        except HTTPException as e:
            if e.status_code == 422:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="User does not exist")

        if not self.crypto.verify(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

        access_token = create_access_token(payload={'user_id': user_id}, role=Role.USER_NOT_AUTH)
        return access_token


    def delete_user(self, user_id):
        user = self.user_repository.find_by_user_id(user_id)
        if not user:
            raise HTTPException(status_code=422, detail="User not found")

        result: int = self.user_repository.delete(user.user_id)
        return result
