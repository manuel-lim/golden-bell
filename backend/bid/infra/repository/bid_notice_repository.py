from sqlalchemy import select

from backend.bid.domain.repository.bid_notice_repository import IBidNoticeRepository
from backend.bid.infra.models.construction_base_price import BasePrice
from backend.bid.infra.models.main_industry import MainIndustry
from backend.common import BidType
from backend.database import SessionLocal
from backend.bid.infra.models.construction import Construction
from backend.bid.domain.dto.construction_dto import ConstructionDTO
from backend.bid.infra.models.service import Service
from backend.bid.infra.models.foreign_procurement import ForeignProcurement
from backend.bid.infra.models.product import Product

from backend.bid.domain.construction import Construction as ConstructionVo
from backend.utils.db_utils import row_to_dict
from backend.utils import integer


class BidNoticeRepository(IBidNoticeRepository):
    def get_construction_list(self, page, per_page, body_data: dict) -> tuple[int, list[ConstructionDTO]]:
        """
        공사명, 종목, 지역, 기초금액/추정가격, 발주처, 현설일, 등록마감일, 협정마감일, 투찰시작일, 개찰일, 입력일, 대업종, 투찰률, 예가범위
        :param page:
        :param per_page:
        :param body_data:
        :return:
        """
        with (SessionLocal() as session):
            query = session.query(Construction.bid_ntce_no,  # 공사 id
                                   Construction.bid_ntce_ord,  # 공사 id seq
                                   Construction.bid_ntce_nm,  # 공사명
                                   MainIndustry.tmp_nm,  # 종목
                                   Construction.cnstrtsite_rgn_nm, # 지역
                                   Construction.bdgt_amt,  # 기초금액 / 예정금액
                                   Construction.presmpt_prce,  # 추정가격
                                   Construction.dminstt_nm,  # 발주처 TODO CHECK.
                                   # 현설일
                                   Construction.bid_qlfct_rgst_dt,  # 등록마감일,
                                   Construction.cmmn_spldmd_agrmnt_clse_dt,  # 협정마감일 TODO CHECK.
                                   Construction.bid_begin_dt,  # 투착시작일
                                   Construction.bid_clse_dt,  # 투착마감일
                                   Construction.openg_dt,  # 개찰일
                                   Construction.rgst_dt,  # 입력일,

                                   BasePrice.rsrvtn_prce_rng_bgn_rate,  # 예가범위1
                                   BasePrice.rsrvtn_prce_rng_end_rate,  # 예가범위2
                                   Construction.sucsfbid_mthd_nm,  # 낙찰방법
                                   Construction.ntce_instt_nm,  # 발주기관
                                   Construction.ntce_instt_ofcl_nm,  # 담당자명
                                   Construction.ntce_instt_ofcl_tel_no,  # 담당자번호
                                   Construction.cntrct_cncls_mthd_nm,  # 계약방법
                                   Construction.contrctrcnstrtn_govsply_mtrl_amt,  # 도급자관금액
                                   Construction.govcnstrtn_govsply_mtrl_amt,  # 관급자관금액
                                   ).join(MainIndustry, Construction.bid_ntce_no == MainIndustry.bid_ntce_no).join(BasePrice, Construction.bid_ntce_no == BasePrice.bid_ntce_no)

            region_name = body_data.get('region_name', '')
            if region_name:
                query = query.filter(Construction.cnstrtsite_rgn_nm.like(f'%{region_name}%'))

            # TODO. 종목에 대한 검색
            construction_name = body_data.get('construction_name', '')
            if construction_name:
                query = query.filter(Construction.bid_ntce_nm.like(f'%{construction_name}%'))

            construction_id = body_data.get('construction_id', '')
            if construction_id:
                query = query.filter(Construction.bid_ntce_no.like(f'%{construction_id}%'))

            from_bdgt_amt = integer(body_data.get('from_bdgt_amt', '0'))  # 최소 예산 금액
            to_bdgt_amt = integer(body_data.get('to_bdgt_amt', '0'))  # 최대 예산 금액

            estimated_type = body_data.get('estimated_type', 'base')
            if from_bdgt_amt and to_bdgt_amt:
                if estimated_type == 'price':
                    query = query.filter(from_bdgt_amt <= Construction.presmpt_prce <= to_bdgt_amt)
                else:  # base
                    query = query.filter(from_bdgt_amt <= Construction.bdgt_amt <= to_bdgt_amt)

            total_count = query.count()
            offset = (page - 1) * per_page
            constructions = query.offset(offset).limit(per_page).all()

            result = [ConstructionDTO(**row_to_dict(c)) for c in constructions]
            return total_count, result
