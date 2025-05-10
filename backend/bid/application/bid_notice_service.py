from typing import Optional

from dependency_injector.wiring import inject
from fastapi import HTTPException, status
from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.bid.domain.construction import Construction as BidConstructionVo
from backend.bid.domain.dto.construction_dto import ConstructionDTO



class BidNoticeService:
    @inject
    def __init__(self, bid_notice_repository: IBidNoticeRepository):
        self.bid_notice_repository = bid_notice_repository

    def create_bid_notice(self):
        pass

    def get_construction_list(self, page, per_page, body_data: dict) -> tuple[int, list[ConstructionDTO]]:
        return self.bid_notice_repository.get_construction_list(page, per_page, body_data)
