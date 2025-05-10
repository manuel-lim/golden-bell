from abc import ABCMeta, abstractmethod
from backend.bid.domain.dto.construction_dto import ConstructionDTO


class IBidNoticeRepository(metaclass=ABCMeta):
    # @abstractmethod
    # def save(self, bid_notice: BidNotice):
    #     raise NotImplementedError

    @abstractmethod
    def get_construction_list(self, page, per_page, body_data: dict) -> tuple[int, list[ConstructionDTO]]:
        raise NotImplementedError
