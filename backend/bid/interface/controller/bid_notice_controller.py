from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from backend.bid.application.bid_service import BidNoticeService
from backend.containers import Container

router = APIRouter(prefix='/bid_notice')

@router.get('/list')
@inject
def get_bid_notices(page: int =1,
                    per_page: int=20,
                    bid_notice_service: BidNoticeService = Depends(Provide[Container.bid_notice_service])):
    total_count, bid_notices = bid_notice_service.get_bid_notices(page, per_page)
    return {'total_count': total_count, 'bid_notices': bid_notices}
