from typing import Optional

from dependency_injector.wiring import inject
from fastapi import HTTPException, status
from backend.bid.domain.repository.bid_repository import IBidRepository
from backend.bid.domain.bid_construction import BidConstruction as BidNoticeConstructionVo

class BidNoticeService:
    @inject
    def __init__(self, bid_notice_repository: IBidRepository):
        self.bid_notice_repository = bid_notice_repository

    def create_bid_notice(self):
        pass

    def get_bid_notices(self, page, per_page, body_data: BidNoticeConstructionVo) -> tuple[int, list[BidNoticeConstructionVo]]:
        return self.bid_notice_repository.get_bid_list(page, per_page, body_data)