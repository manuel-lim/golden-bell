from typing import Optional
from dataclasses import dataclass
from backend.bid.domain import Bid


"""
검색조건에 변경일시, 입찰공고번호를 입력하여 변경된 입찰공고번호, 입찰공고차수, 입찰분류번호, 재입찰번호, 
변경항목명, 변경전후값 등 물품 입찰공고변경 데이터 조회 
※ 변경이력 추출 대상 항목 PQ신청서접수일시, 물품분류제한여부, 제조여부, 입찰서개시일시, 입찰서마감일시, 개찰일시, 입찰자격등록일시, 
공동수급협정서마감일시, PQ신청서접수방법명, 참가가능지역, 면허제한코드, 설명회실시일시, 입찰참가제한여부, 공고서, 규격서, 공고규격화일, 
공동수급구성방식코드, 입찰계약방법코드, 공동수급구성방식,실적신청서접수일시, 공고명, 재입찰허용여부, 실적신청서접수방법코드,예가방법구분코드, 
집행관코드, 추첨복수예가개수, 배정예산금액,총예가개수, 추정가격, 내역입찰여부, 지사투찰허용여부
"""

@dataclass
class BidProductHistory(Bid):
    bsns_div_nm: Optional[str] = None  # 업무구분명
    chg_data_div_nm: Optional[str] = None  # 변경데이터구분명
    chg_dt: Optional[str] = None  # 변경일시
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    chg_item_nm: Optional[str] = None  # 변경항목명
    bfchg_val: Optional[str] = None  # 변경전값
    afchg_val: Optional[str] = None  # 변경후값
    lcns_lmt_cd_rgst_list: Optional[str] = None  # 면허제한코드등록목록
