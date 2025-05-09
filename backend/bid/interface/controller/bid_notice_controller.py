from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from backend.bid.application.bid_notice_service import BidNoticeService
from backend.bid.interface.controller import BidNoticeBody, GetBidNoticeResponse, BidNoticeBody, GetBidNoticeConstructionResponse
from backend.containers import Container
from backend.bid.domain.bid_construction import BidConstruction as BidConstructionVo
from backend.utils import props

router = APIRouter(prefix='/bid_notice')

@router.get('/list/constructions')
@inject
def get_bid_notices_constructions(
        body_data: BidNoticeBody = Depends(),
                    bid_notice_service: BidNoticeService = Depends(Provide[Container.bid_notice_service])) -> GetBidNoticeConstructionResponse:

    total_count, bid_notices = bid_notice_service.get_bid_construction_list(body_data.page, body_data.per_page, props(body_data))
    return GetBidNoticeConstructionResponse(total_count=total_count, data=bid_notices)

