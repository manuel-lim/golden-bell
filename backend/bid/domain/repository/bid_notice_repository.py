from abc import ABCMeta, abstractmethod

class IBidNoticeRepository(metaclass=ABCMeta):
    # @abstractmethod
    # def save(self, bid_notice: BidNotice):
    #     raise NotImplementedError

    @abstractmethod
    def get_bid_notices(self, page, per_page, body_data: dict) -> tuple[int, list[dict]]:
        raise NotImplementedError
