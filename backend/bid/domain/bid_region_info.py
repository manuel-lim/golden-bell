from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


# 참가가능지역정보조회
@dataclass
class BidRegionInfo(BaseModel):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    lmt_sno: Optional[str] = None  # 제한순번
    prtcpt_psbl_rgn_nm: Optional[str] = None  # 참가가능지역명
    rgst_dt: Optional[str] = None  # 등록일시
    bsns_div_nm: Optional[str] = None  # 업무구분명