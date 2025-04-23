from abc import ABCMeta, abstractmethod
from backend.user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_by_user_id(self, user_id: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_users(self, page: int, per_page: int) -> tuple[int, list[User]]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: str) -> bool:
        raise NotImplementedError
