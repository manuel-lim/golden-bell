from abc import ABCMeta, abstractmethod
from backend.bid.domain.bid_notice_construction import BidNoticeConstruction as BidNoticeConstructionVo

class IBidNoticeRepository(metaclass=ABCMeta):
    # @abstractmethod
    # def save(self, bid_notice: BidNotice):
    #     raise NotImplementedError

    @abstractmethod
    def get_bid_notices(self, page, per_page, body_data: BidNoticeConstructionVo) -> tuple[int, list[BidNoticeConstructionVo]]:
        raise NotImplementedError
