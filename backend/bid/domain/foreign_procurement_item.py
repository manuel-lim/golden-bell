from typing import Optional
from dataclasses import dataclass
from backend.bid.domain import Bid


"""
입찰공고목록 정보에 대한 외자 구매대상물품조회
"""

@dataclass
class ForeignProcurementItem(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    prdct_sno: Optional[str] = None  # 물품순번
    dminstt_cd: Optional[str] = None  # 수요기관코드
    dminstt_nm: Optional[str] = None  # 수요기관명
    hsk_no: Optional[str] = None  # HSK번호
    dtil_prdct_clsfc_no: Optional[str] = None  # 세부품명번호
    dtil_prdct_clsfc_no_nm: Optional[str] = None  # 세부품명
    qty: Optional[str] = None  # 수량
    unit: Optional[str] = None  # 단위
    asign_amt: Optional[str] = None  # 배정금액
    asign_amt_crncy: Optional[str] = None  # 배정금액통화
    ntce_ntice_dt: Optional[str] = None  # 공고게시일시
    dlvry_cndtn_nm: Optional[str] = None  # 인도조건명
    prdct_clsfc_no: Optional[str] = None  # 물품분류번호
    prdct_clsfc_no_nm: Optional[str] = None  # 물품분류명
    prdct_spec_nm: Optional[str] = None  # 규격명
    uprc: Optional[str] = None  # 단가
    dlvr_tmlmt_dt: Optional[str] = None  # 납기일자
    dlvr_daynum: Optional[str] = None  # 납기일수
    dlvr_plce: Optional[str] = None  # 납품장소
