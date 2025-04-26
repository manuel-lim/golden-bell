from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.common import BidType
from backend.database import SessionLocal
from backend.bid.infra.models.bid_notice_construction import BidNoticeConstruction
from backend.bid.infra.models.bid_notice_outsourcing import BidNoticeOutsourcing
from backend.bid.infra.models.bid_notice_imported_goods import BidNoticeImportedGoods
from backend.bid.infra.models.bid_notice_product import BidNoticeProduct

from backend.bid.domain.bid_notice_construction import BidNoticeConstruction as BidNoticeConstructionVo
from backend.utils.db_utils import row_to_dict


class BidNoticeRepository(IBidNoticeRepository):
    def get_bid_notices(self, page, per_page, body_data: dict) -> tuple[int, list[dict]]:
        with SessionLocal() as session:
            bid_type = body_data.get('bid_type')

            base = BidNoticeConstruction
            if bid_type is BidType.OUTSOURCING:
                base = BidNoticeOutsourcing
            elif bid_type is BidType.IMPORTED:
                base = BidNoticeImportedGoods
            elif bid_type is BidType.PRODUCT:
                base = BidNoticeProduct

            query = session.query(base)
            total_count = query.count()

            try:
                from_bdgt_amt = int(body_data.get('from_bdgt_amt', '0'))  # 최소 예산 금액
                to_bdgt_amt = int(body_data.get('to_bdgt_amt', '0'))  # 최대 예산 금액

            except ValueError:  # TODO LOG.
                pass

            # 금액
            if from_bdgt_amt and to_bdgt_amt:
                if base is BidNoticeConstruction:
                    query = query.where(from_bdgt_amt <= BidNoticeConstruction.bdgt_amt <= to_bdgt_amt)
                else:
                    query = query.where(from_bdgt_amt <= int(base.asign_bdgt_amt) <= to_bdgt_amt)

            offset = (page - 1) * per_page
            bid_notices = query.limit(per_page).offset(offset).all()

            # TODO. 검색조건
            # 개찰일, 입력일, 공사명/공고번호 / 발주처 / 수요기관 / 정렬방법 / 금액(예산액) / 사업명 / 업무구분 (물품, 공사, 용역, 외자)

            return total_count, bid_notices
