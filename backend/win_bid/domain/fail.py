from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass


"""
개찰결과 유찰 목록 조회 /getOpengResultListInfoFailing

검색조건을 입찰공고번호 입력하여 물품, 공사, 용역, 외자의 나라장터 개찰결과 유찰 목록
(개찰결과구분명, 입찰공고번호, 입찰공고차수, 입찰분류번호, 재입찰번호, 유찰사유)을 조회
"""

@dataclass
class Fail(BaseModel):
    openg_rslt_div_nm: Optional[str] = None  # 개찰결과구분명
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    nobid_rsn: Optional[str] = None  # 유찰사유
