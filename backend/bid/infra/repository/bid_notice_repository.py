from sqlalchemy import select

from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.bid.infra.models.bid_base_price import BidBasePrice
from backend.bid.infra.models.bid_main_industry import BidMainIndustry
from backend.common import BidType
from backend.database import SessionLocal
from backend.bid.infra.models.bid_construction import BidConstruction
from backend.bid.domain.dto.bid_construction_dto import BidConstructionDTO
from backend.bid.infra.models.bid_service import BidService
from backend.bid.infra.models.bid_foreign_procurement import BidForeignProcurement
from backend.bid.infra.models.bid_product import BidProduct

from backend.bid.domain.bid_construction import BidConstruction as BidConstructionVo
from backend.utils.db_utils import row_to_dict
from backend.utils import integer


class BidNoticeRepository(IBidNoticeRepository):
    def get_bid_construction_list(self, page, per_page, body_data: dict) -> tuple[int, list[BidConstructionDTO]]:
        """
        공사명, 종목, 지역, 기초금액/추정가격, 발주처, 현설일, 등록마감일, 협정마감일, 투찰시작일, 개찰일, 입력일, 대업종, 투찰률, 예가범위
        :param page:
        :param per_page:
        :param body_data:
        :return:
        """
        with (SessionLocal() as session):
            query = session.query(BidConstruction.bid_ntce_no,  # 공사 id
                                   BidConstruction.bid_ntce_ord,  # 공사 id seq
                                   BidConstruction.bid_ntce_nm,  # 공사명
                                   BidMainIndustry.tmp_nm,  # 종목
                                   BidConstruction.cnstrtsite_rgn_nm, # 지역
                                   BidConstruction.bdgt_amt,  # 기초금액
                                   BidConstruction.presmpt_prce,  # 추정가격
                                   BidConstruction.dminstt_nm,  # 발주처 TODO CHECK.
                                   # 현설일
                                   BidConstruction.bid_qlfct_rgst_dt,  # 등록마감일,
                                   BidConstruction.cmmn_spldmd_agrmnt_clse_dt,  # 협정마감일 TODO CHECK.
                                   BidConstruction.bid_begin_dt,  # 투착시작일
                                   BidConstruction.bid_clse_dt,  # 투착마감일
                                   BidConstruction.openg_dt,  # 개찰일
                                   BidConstruction.rgst_dt,  # 입력일,

                                   BidBasePrice.rsrvtn_prce_rng_bgn_rate,  # 예가범위1
                                   BidBasePrice.rsrvtn_prce_rng_end_rate,  # 예가범위2
                                   ).join(BidMainIndustry, BidConstruction.bid_ntce_no == BidMainIndustry.bid_ntce_no).join(BidBasePrice, BidConstruction.bid_ntce_no == BidBasePrice.bid_ntce_no)

            region_name = body_data.get('region_name', '')
            if region_name:
                query = query.filter(BidConstruction.cnstrtsite_rgn_nm.like(f'%{region_name}%'))

            # TODO. 종목에 대한 검색
            construction_name = body_data.get('construction_name', '')
            if construction_name:
                query = query.filter(BidConstruction.bid_ntce_nm.like(f'%{construction_name}%'))

            construction_id = body_data.get('construction_id', '')
            if construction_id:
                query = query.filter(BidConstruction.bid_ntce_no.like(f'%{construction_id}%'))

            from_bdgt_amt = integer(body_data.get('from_bdgt_amt', '0'))  # 최소 예산 금액
            to_bdgt_amt = integer(body_data.get('to_bdgt_amt', '0'))  # 최대 예산 금액

            estimated_type = body_data.get('estimated_type', 'base')
            if from_bdgt_amt and to_bdgt_amt:
                if estimated_type == 'price':
                    query = query.filter(from_bdgt_amt <= BidConstruction.presmpt_prce <= to_bdgt_amt)
                else:  # base
                    query = query.filter(from_bdgt_amt <= BidConstruction.bdgt_amt <= to_bdgt_amt)

            total_count = query.count()
            offset = (page - 1) * per_page
            constructions = query.offset(offset).limit(per_page).all()

            result = [BidConstructionDTO(**row_to_dict(c)) for c in constructions]
            return total_count, result
