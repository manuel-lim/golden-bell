from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class ProductOpenResult(BaseModel):
    id: Optional[int] = None  # 고유 ID (자동 증가)
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
    created_at: Optional[str] = None  # 생성일시
