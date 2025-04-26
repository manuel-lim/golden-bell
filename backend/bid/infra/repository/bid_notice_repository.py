from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.database import SessionLocal
from backend.bid.infra.models.bid_notice_construction import BidNoticeConstruction
from backend.bid.domain.bid_notice_construction import BidNoticeConstruction as BidNoticeConstructionVo
from backend.utils.db_utils import row_to_dict


class BidNoticeRepository(IBidNoticeRepository):
    def get_bid_notices(self, page, per_page, body_data: BidNoticeConstructionVo) -> tuple[int, list[BidNoticeConstructionVo]]:
        with SessionLocal() as session:
            query = session.query(BidNoticeConstruction)
            total_count = query.count()

            offset = (page - 1) * per_page
            bid_notices = query.limit(per_page).offset(offset).all()

            # TODO. 검색조건
            # 개찰일, 입력일, 공사명/공고번호 / 발주처 / 수요기관 / 정렬방법 / 금액(예산액) / 사업명 / 업무구분 (물품, 공사, 용역, 외자)
            bid_notices = [BidNoticeConstructionVo(**row_to_dict(bid)) for bid in bid_notices]
            return total_count, bid_notices
