from abc import ABCMeta, abstractmethod
from backend.bid.domain.bid_notice import BidNotice

class IBidNoticeRepository(metaclass=ABCMeta):
    # @abstractmethod
    # def save(self, bid_notice: BidNotice):
    #     raise NotImplementedError

    @abstractmethod
    def get_bid_notices(self, page: int, per_page: int) -> tuple[int, list[BidNotice]]:
        raise NotImplementedError
