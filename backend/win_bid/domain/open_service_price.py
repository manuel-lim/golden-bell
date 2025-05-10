from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass


@dataclass
class OpenServicePrice(BaseModel):
    id: Optional[int] = None  # 고유 ID (자동 증가)
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    bid_ntce_nm: Optional[str] = None  # 입찰공고명
    plnprc: Optional[str] = None  # 예정가격
    bssamt: Optional[str] = None  # 기초금액
    tot_rsrvtn_prce_num: Optional[str] = None  # 총예가건수
    compno_rsrvtn_prce_sno: Optional[str] = None  # 복수예가순번
    bsis_plnprc: Optional[str] = None  # 기초예정가격
    drwt_yn: Optional[str] = None  # 추첨여부
    drwt_num: Optional[str] = None  # 추첨횟수
    bidwinr_slctn_apl_bss_cntnts: Optional[str] = None  # 최종낙찰자선정적용기준내용
    rl_openg_dt: Optional[str] = None  # 실개찰일시
    bssamt_bss_up_num: Optional[str] = None  # 기초금액기준상위건수
    compno_rsrvtn_prce_mkng_dt: Optional[str] = None  # 복수예비가격작성일시
    inpt_dt: Optional[str] = None  # 입력일시
    prearng_prce_purcnstcst: Optional[str] = None  # 예정가격순공사비
    created_at: Optional[str] = None  # 생성일시