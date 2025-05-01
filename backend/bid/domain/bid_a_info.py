from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


# 입찰가격산식A정보 조회
@dataclass
class BidAInfo(Bid):
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
