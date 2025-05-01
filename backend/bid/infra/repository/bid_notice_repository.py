from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.common import BidType
from backend.database import SessionLocal
from backend.bid.infra.models.bid_construction import BidConstruction
from backend.bid.infra.models.bid_outsourcing import BidOutsourcing
from backend.bid.infra.models.bid_imported_goods import BidImportedGoods
from backend.bid.infra.models.bid_product import BidProduct

from backend.bid.domain.bid_construction import BidConstruction as BidConstructionVo
from backend.utils.db_utils import row_to_dict


class BidRepository(IBidNoticeRepository):
    def get_bid_list(self, page, per_page, body_data: dict) -> tuple[int, list[dict]]:
        with SessionLocal() as session:
            bid_type = body_data.get('bid_type')

            base = BidConstruction
            if bid_type is BidType.OUTSOURCING:
                base = BidOutsourcing
            elif bid_type is BidType.IMPORTED:
                base = BidImportedGoods
            elif bid_type is BidType.PRODUCT:
                base = BidProduct

            query = session.query(base)
            total_count = query.count()

            try:
                from_bdgt_amt = int(body_data.get('from_bdgt_amt', '0'))  # 최소 예산 금액
                to_bdgt_amt = int(body_data.get('to_bdgt_amt', '0'))  # 최대 예산 금액

            except ValueError:  # TODO LOG.
                pass

            # 금액
            if from_bdgt_amt and to_bdgt_amt:
                if base is BidConstruction:
                    query = query.where(from_bdgt_amt <= BidConstruction.bdgt_amt <= to_bdgt_amt)
                else:
                    query = query.where(from_bdgt_amt <= int(base.asign_bdgt_amt) <= to_bdgt_amt)

            offset = (page - 1) * per_page
            bid_notices = query.limit(per_page).offset(offset).all()

            # TODO. 검색조건
            # 개찰일, 입력일, 공사명/공고번호 / 발주처 / 수요기관 / 정렬방법 / 금액(예산액) / 사업명 / 업무구분 (물품, 공사, 용역, 외자)

            return total_count, bid_notices
