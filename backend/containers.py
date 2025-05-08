from dependency_injector import containers, providers

from backend.bid.application.bid_notice_service import BidNoticeService
from backend.bid.infra.repository.bid_notice_repository import BidNoticeRepository
from backend.user.application.user_service import UserService
from backend.user.infra.repository.user_repository import UserRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['backend.user', 'backend.bid'])
    user_repository = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, user_repository=user_repository)

    bid_notice_repository = providers.Factory(BidNoticeRepository)
    bid_notice_service = providers.Factory(BidNoticeService, bid_notice_repository=bid_notice_repository)
