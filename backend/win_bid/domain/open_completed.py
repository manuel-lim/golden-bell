from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass


@dataclass
class OpenCompleted(BaseModel):
    id: Optional[int] = None  # 고유 ID (자동 증가)
    openg_rslt_div_nm: Optional[str] = None  # 개찰결과구분명
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    openg_rank: Optional[str] = None  # 개찰순위
    prcbdr_bizno: Optional[str] = None  # 투찰업체사업자등록번호
    prcbdr_nm: Optional[str] = None  # 투찰업체명
    prcbdr_ceo_nm: Optional[str] = None  # 투찰업체대표자명
    bidprc_amt: Optional[str] = None  # 투찰금액
    bidprcrt: Optional[str] = None  # 투찰률
    rmrk: Optional[str] = None  # 비고
    cnstty_accot_bid_amt_url: Optional[str] = None  # 공종별입찰금액URL
    drwt_no1: Optional[str] = None  # 추첨번호1
    drwt_no2: Optional[str] = None  # 추첨번호2
    bidprc_dt: Optional[str] = None  # 투찰일시
    created_at: Optional[str] = None  # 생성일시