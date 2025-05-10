from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid

"""
입찰공고목록 정보에 대한 입찰가격산식A정보조회 /getBidPblancListBidPrceCalclAInfo

검색조건에 공고게시일시와 입찰공고번호를 입력하여 입찰가격산식 A값 적용 
공고의 합산항목인 국민연금보험료, 국민건강보험료, 퇴직공제부금비, 노인장기요양보험료, 
산업안전보건관리비, 안전관리비, 품질관리비, 품질관리비 적용대상여부등 입찰가격산식A정보 조회 ( 복수예가는 A값 공개 시 제공)
"""

@dataclass
class AInfo(Bid):
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    sfty_mngcst: Optional[str] = None
    sfty_chck_mngcst: Optional[str] = None
    rtrfund_non: Optional[str] = None
    mrfn_health_insrprm: Optional[str] = None
    npn_insrprm: Optional[str] = None
    odsn_lngtrmrcpr_insrprm: Optional[str] = None
    qlty_mngcst: Optional[str] = None
    qlty_mngcst_a_obj_yn: Optional[str] = None
    prearng_prce_dcsn_mthd_nm: Optional[str] = None
    ntce_ntice_dt: Optional[str] = None
    bid_prce_calcl_a_open_dt: Optional[str] = None
