from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class Rebid(BaseModel):
    openg_rslt_div_nm: Optional[str] = None  # 개찰결과구분명
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    bid_clse_dt: Optional[str] = None  # 입찰마감일시
    openg_dt: Optional[str] = None  # 개찰일시
    rbid_rsn: Optional[str] = None  # 재입찰사유
    cmmn_spldmd_agrmnt_clse_dt: Optional[str] = None  # 공동수급혐정마감일시