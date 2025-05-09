from abc import ABCMeta, abstractmethod
from backend.bid.domain.dto.bid_construction_dto import BidConstructionDTO


class IBidNoticeRepository(metaclass=ABCMeta):
    # @abstractmethod
    # def save(self, bid_notice: BidNotice):
    #     raise NotImplementedError

    @abstractmethod
    def get_bid_construction_list(self, page, per_page, body_data: dict) -> tuple[int, list[BidConstructionDTO]]:
        raise NotImplementedError


    @abstractmethod
    def get_bid_construction(self, bid_construction_id: str) -> BidConstructionDTO:
        raise NotImplementedError