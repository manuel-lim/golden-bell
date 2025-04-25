from abc import ABCMeta, abstractmethod
from backend.bid.domain.bid_notice import BidNotice as BidNoticeVo

class IBidNoticeRepository(metaclass=ABCMeta):
    # @abstractmethod
    # def save(self, bid_notice: BidNotice):
    #     raise NotImplementedError

    @abstractmethod
    def get_bid_notices(self, page, per_page, body_data: BidNoticeVo) -> tuple[int, list[BidNoticeVo]]:
        raise NotImplementedError
