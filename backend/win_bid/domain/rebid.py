from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass


"""
개찰결과 재입찰 목록 조회 /getOpengResultListInfoRebid

검색조건을 입찰공고번호 입력하여 물품, 공사, 용역, 외자의 나라장터 개찰결과 재입찰 목록(개찰결과구분명, 입찰공고번호, 
입찰공고차수, 입찰분류번호, 재입찰번호, 입찰마감일시, 개찰일시, 재입찰사유, 공동수급협정마감일시)을 조회.
"""

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