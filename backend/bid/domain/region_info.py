from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


"""
입찰공고목록 정보에 대한 참가가능지역정보조회 /getBidPblancListInfoPrtcptPsblRgn
검색조건에 등록일시범위(통합입찰공고)와 입찰공고번호를 입력하여 입찰공고번호, 입찰공고차수, 제한그룹번호, 참가가능지역명, 등록일시 등 참가가능지역정보조회
"""

@dataclass
class RegionInfo(BaseModel):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    lmt_sno: Optional[str] = None  # 제한순번
    prtcpt_psbl_rgn_nm: Optional[str] = None  # 참가가능지역명
    rgst_dt: Optional[str] = None  # 등록일시
    bsns_div_nm: Optional[str] = None  # 업무구분명