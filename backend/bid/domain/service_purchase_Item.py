from typing import Optional
from backend.bid.domain import Bid
from dataclasses import dataclass


"""
검색조건에 등록일시범위(통합입찰공고)와 입찰공고번호를 입력하여 입찰공고번호, 
입찰공고차수, 입찰분류번호, 물품순번, 수요기관코드, 수요기관명, 물품분류번호, 
품명, 세부품명번호, 세부품명, 수량, 단위, 단가, 납품기한일시, 납품일수, 납품장소, 인도조건명 등 용역 구매대상물품 정보 조회
"""
@dataclass
class ServicePurchaseItem(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    prdct_sno: Optional[str] = None  # 물품순번
    dminstt_cd: Optional[str] = None  # 수요기관코드
    dminstt_nm: Optional[str] = None  # 수요기관명
    prdct_clsfc_no: Optional[str] = None  # 물품분류번호
    prdct_clsfc_no_nm: Optional[str] = None  # 품명
    dtil_prdct_clsfc_no: Optional[str] = None  # 세부품명번호
    dtil_prdct_clsfc_no_nm: Optional[str] = None  # 세부품명
    prdct_spec_nm: Optional[str] = None  # 물품규격명
    qty: Optional[str] = None  # 수량
    unit: Optional[str] = None  # 단위
    uprc: Optional[str] = None  # 단가
    dlvr_tmlmt_dt: Optional[str] = None  # 납품기한일시
    dlvr_daynum: Optional[str] = None  # 납품일수
    dlvr_plce: Optional[str] = None  # 납품장소
    dlvry_cndtn_nm: Optional[str] = None  # 인도조건명
    ntce_ntice_dt: Optional[str] = None  # 공고게시일시