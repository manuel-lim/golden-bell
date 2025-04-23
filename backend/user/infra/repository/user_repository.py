import traceback

from fastapi import HTTPException
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from backend.database import SessionLocal
from backend.user.domain.repository.user_repository import IUserRepository
from backend.user.domain.user import User as UserVo
from backend.user.infra.models.user import User
from backend.utils.db_utils import row_to_dict
from backend.utils import props

class UserRepository(IUserRepository):
    def save(self, user: UserVo):
        new_user = User(**props(user))
        with SessionLocal() as session:
            try:
                session.add(new_user)
                session.commit()
            except IntegrityError as e:
                session.rollback()
                raise HTTPException(status_code=400, detail=str(e))

            except SQLAlchemyError as e:
                session.rollback()
                raise HTTPException(status_code=500, detail=str(e))
            finally:
                session.close()

    def find_by_user_id(self, user_id: str) -> UserVo:
        with SessionLocal() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if not user:
                raise HTTPException(status_code=422, detail="User not found")

            return UserVo(**row_to_dict(user))

    def update(self, user_vo: UserVo) -> UserVo:
        with SessionLocal() as session:
            user = session.query(User).filter(User.user_id == user_vo.user_id).first()
            if not user:
                raise HTTPException(status_code=422, detail="User not found")

            session.add(user)
            session.commit()

            return user_vo

    def get_users(self, page: int, per_page: int) -> tuple[int, list[User]]:
        with SessionLocal() as session:
            query = session.query(User)
            total_count = query.count()

            offset = (page - 1) * per_page
            users = query.limit(per_page).offset(offset).all()
            return total_count, users

    def delete(self, user_id: str):
        with SessionLocal() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if not user:
                raise HTTPException(status_code=422, detail="User not found")

            user.status = 0
            session.add(user)
            session.commit()

            return user.status == 0