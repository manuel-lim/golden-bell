from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.database import SessionLocal
from backend.bid.infra.models.bid_notice import BidNotice
from backend.bid.domain.bid_notice import BidNotice as BidNoticeVo
from backend.utils.db_utils import row_to_dict


class BidNoticeRepository(IBidNoticeRepository):
    def get_bid_notices(self, page, per_page, body_data: BidNoticeVo) -> tuple[int, list[BidNoticeVo]]:
        with SessionLocal() as session:
            query = session.query(BidNotice)
            total_count = query.count()

            offset = (page - 1) * per_page
            bid_notices = query.limit(per_page).offset(offset).all()
            bid_notices = [BidNoticeVo(**row_to_dict(bid)) for bid in bid_notices]
            return total_count, bid_notices
