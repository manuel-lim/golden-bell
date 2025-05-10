from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


"""
유찰, 개찰완료, 재입찰건에 대한 개찰결과를 제공하며 검색조건을 공고일시, 개찰일시, 입찰공고번호, 입찰공고명, 공고기관코드, 공고기관명, 수요기관코드, 
수요기관명, 참조번호, 참가제한지역코드, 참가제한지역명, 업종코드, 업종명, 추정가격시작, 추정가격종료, 세부품명번호, 다수공급경쟁자여부, 조달요청번호, 
국제구분코드로하여 용역에 대한 나라장터 개찰결과 목록(입찰공고번호, 입찰공고명, 개찰일시, 참가업체수, 개찰업체정보, 진행구분코드명, 입력일시, 
예비가격파일존재여부, 공고기관명, 수요기관명)을 조회
"""

@dataclass
class G2BServiceResult(BaseModel):
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    bid_clsfc_no: Optional[str] = None
    rbid_no: Optional[str] = None
    bid_ntce_nm: Optional[str] = None
    openg_dt: Optional[str] = None
    prtcpt_cnum: Optional[str] = None
    openg_corp_info: Optional[str] = None
    progrs_div_cd_nm: Optional[str] = None
    inpt_dt: Optional[str] = None
    rsrvtn_prce_file_existnce_yn: Optional[str] = None
    ntce_instt_cd: Optional[str] = None
    ntce_instt_nm: Optional[str] = None
    dminstt_cd: Optional[str] = None
    dminstt_nm: Optional[str] = None
    openg_rslt_ntc_cntnts: Optional[str] = None