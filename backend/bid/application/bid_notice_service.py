from typing import Optional

from dependency_injector.wiring import inject
from fastapi import HTTPException, status
from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.bid.domain.construction import Construction as BidConstructionVo
from backend.bid.domain.dto.construction_dto import BidConstructionDTO



class BidNoticeService:
    @inject
    def __init__(self, bid_notice_repository: IBidNoticeRepository):
        self.bid_notice_repository = bid_notice_repository

    def create_bid_notice(self):
        pass

    def get_bid_construction_list(self, page, per_page, body_data: dict) -> tuple[int, list[BidConstructionDTO]]:
        return self.bid_notice_repository.get_bid_construction_list(page, per_page, body_data)

    def get_bid_construction(self, bid_construction_id: str) -> BidConstructionDTO:
        return self.bid_notice_repository.get_bid_construction(bid_construction_id)
