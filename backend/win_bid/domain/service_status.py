from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass


"""
낙찰된 목록 현황 용역조회 /getScsbidListSttusServc

검색조건을 등록일시, 공고일시, 개찰일시, 입찰공고번호로 용역에 대한 나라장터 최종낙찰자 목록(입찰공고번호, 입찰공고명, 참가업체수, 
최종낙찰업체명, 사업자번호, 최종낙찰률, 실개찰일시, 수요기관, 최종낙찰일, 최종낙찰업체담당자)을 조회
"""

@dataclass
class ServiceStatus(BaseModel):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    ntce_div_cd: Optional[str] = None  # 공고구분코드
    bid_ntce_nm: Optional[str] = None  # 입찰공고명
    prtcpt_cnum: Optional[str] = None  # 참가업체수
    bidwinnr_nm: Optional[str] = None  # 최종낙찰업체명
    bidwinnr_bizno: Optional[str] = None  # 최종낙찰업체사업자등록번호
    bidwinnr_ceo_nm: Optional[str] = None  # 최종낙찰업체대표자명
    bidwinnr_adrs: Optional[str] = None  # 최종낙찰업체주소
    bidwinnr_tel_no: Optional[str] = None  # 최종낙찰업체전화번호
    sucsfbid_amt: Optional[str] = None  # 최종낙찰금액
    sucsfbid_rate: Optional[str] = None  # 최종낙찰률
    rl_openg_dt: Optional[str] = None  # 실개찰일시
    dminstt_cd: Optional[str] = None  # 수요기관코드
    dminstt_nm: Optional[str] = None  # 수요기관명
    rgst_dt: Optional[str] = None  # 등록일시
    fnl_sucsf_date: Optional[str] = None  # 최종낙찰일자
    fnl_sucsf_corp_ofcl: Optional[str] = None  # 최종낙찰업체담당자
    created_at: Optional[str] = None  # 생성일시