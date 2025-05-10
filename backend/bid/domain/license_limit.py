from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


"""
입찰공고목록 정보에 대한 면허제한정보조회 /getBidPblancListInfoLicenseLimit
검색조건에 등록일시범위(통합입찰공고)와 입찰공고번호를 입력하여 입찰공고번호, 입찰공고차수, 
제한그룹번호, 제한순번, 면허제한명, 허용업종목록, 등록일시를 포함한 면허제한정보 조회
"""

@dataclass
class LicenseLimit(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    lmt_grp_no: Optional[str] = None  # 제한그룹번호
    lmt_sno: Optional[str] = None  # 제한순번
    lcns_lmt_nm: Optional[str] = None  # 면허제한명
    permsn_indstryty_list: Optional[str] = None  # 허용업종목록
    rgst_dt: Optional[str] = None  # 등록일시
    bsns_div_nm: Optional[str] = None  # 업무구분명
    indstryty_mfrc_fld_list: Optional[str] = None  # 주력업종분야목록
