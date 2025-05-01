from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


# 면허제한정보조회
@dataclass
class BidLicenseLimit(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    lmt_grp_no: Optional[str] = None  # 제한그룹번호
    lmt_sno: Optional[str] = None  # 제한순번
    lcns_lmt_nm: Optional[str] = None  # 면허제한명
    permsn_indstryty_list: Optional[str] = None  # 허용업종목록
    rgst_dt: Optional[str] = None  # 등록일시
    bsns_div_nm: Optional[str] = None  # 업무구분명
    indstryty_mfrc_fld_list: Optional[str] = None  # 주력업종분야목록
