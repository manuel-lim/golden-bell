from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from backend.bid.application.bid_notice_service import BidNoticeService
from backend.bid.interface.controller import GetBidNoticeBody, GetBidNoticeResponse
from backend.containers import Container
from backend.bid.domain.bid_notice import BidNotice as BidNoticeVo


router = APIRouter(prefix='/bid_notice')

@router.post('/list')
@inject
def get_bid_notices(body_data: Optional[GetBidNoticeBody] = None,
                    bid_notice_service: BidNoticeService = Depends(Provide[Container.bid_notice_service])) -> GetBidNoticeResponse:
    page = body_data.page
    per_page = body_data.per_page
    bid_notice = BidNoticeVo(**body_data.body.model_dump(exclude_none=True))

    total_count, bid_notices = bid_notice_service.get_bid_notices(page, per_page, bid_notice)

    return GetBidNoticeResponse(total_count=total_count, data=bid_notices)

