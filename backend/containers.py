from dependency_injector import containers, providers
from backend.user.application.user_service import UserService
from backend.user.infra.repository.user_repository import UserRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['backend.user'])
    user_repository = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
