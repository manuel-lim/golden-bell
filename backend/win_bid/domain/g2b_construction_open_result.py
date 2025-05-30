from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel

"""
나라장터 검색조건에 의한 개찰결과 공사 목록 조회 /getOpengResultListInfoCnstwkPPSSrch

유찰, 개찰완료, 재입찰건에 대한 개찰결과를 제공하며 검색조건을 공고일시, 개찰일시, 입찰공고번호, 입찰공고명, 공고기관코드, 공고기관명, 수요기관코드, 
수요기관명, 참조번호, 참가제한지역코드, 참가제한지역명, 업종코드, 업종명, 추정가격시작, 추정가격종료, 세부품명번호, 다수공급경쟁자여부, 조달요청번호, 
국제구분코드로 하여 공사에 대한 나라장터 개찰결과 목록(입찰공고번호, 입찰공고명, 개찰일시, 참가업체수, 개찰업체정보, 진행구분코드명, 입력일시, 
예비가격파일존재여부, 공고기관명, 수요기관명)을 조회
"""


@dataclass
class G2BConstructionOpenResult(BaseModel):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    bid_ntce_nm: Optional[str] = None  # 입찰공고명
    openg_dt: Optional[str] = None  # 개찰일시
    prtcpt_cnum: Optional[str] = None  # 참가업체수
    openg_corp_info: Optional[str] = None  # 개찰업체정보
    progrs_div_cd_nm: Optional[str] = None  # 진행구분코드명
    inpt_dt: Optional[str] = None  # 입력일시
    rsrvtn_prce_file_existnce_yn: Optional[str] = None  # 예비가격파일존재여부
    ntce_instt_cd: Optional[str] = None  # 공고기관코드
    ntce_instt_nm: Optional[str] = None  # 공고기관명
    dminstt_cd: Optional[str] = None  # 수요기관코드
    dminstt_nm: Optional[str] = None  # 수요기관명
    openg_rslt_ntc_cntnts: Optional[str] = None  # 개찰결과공지내용
