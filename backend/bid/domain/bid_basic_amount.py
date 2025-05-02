from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


"""
검색조건에 기초금액 등록일시, 입찰공고번호를 입력하여 입찰공고번호, 입찰공고명, 기초금액, 기초금액공개일시, 
예비가격범위시작율, 평가기준금액, 난이도계수, 기타경비기준율 등 물품의 기초금액정보 조회
"""
@dataclass
class BidBasicAmount(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    bid_ntce_nm: Optional[str] = None  # 입찰공고명
    bssamt: Optional[str] = None  # 기초금액
    bssamt_open_dt: Optional[str] = None  # 기초금액공개일시
    rsrvtn_prce_rng_bgn_rate: Optional[str] = None  # 예비가격범위시작률
    rsrvtn_prce_rng_end_rate: Optional[str] = None  # 예비가격범위종료율
    evl_bss_amt: Optional[str] = None  # 평가기준금액
    dfcltydgr_cfcnt: Optional[str] = None  # 난이도계수
    etc_gnrlexpns_bss_rate: Optional[str] = None  # 기타경비기준율
    gnrl_mngcst_bss_rate: Optional[str] = None  # 일반관리비기준율
    prft_bss_rate: Optional[str] = None  # 이윤기준율
    lbrcst_bss_rate: Optional[str] = None  # 노무비기준율
    indust_sfty_helth_mngcst: Optional[str] = None  # 산업안전보건관리비
    rtrfund_non: Optional[str] = None  # 퇴직공제부금비
    env_cnsrvcst: Optional[str] = None  # 환경보전비
    scontrct_payprce_pay_grnty_fee: Optional[str] = None  # 하도급대금지급보증수수료
    mrfn_health_insrprm: Optional[str] = None  # 국민건강보험료
    npn_insrprm: Optional[str] = None  # 국민연금보험료
    rmrk1: Optional[str] = None  # 비고1
    rmrk2: Optional[str] = None  # 비고2
    useful_amt: Optional[str] = None  # 가용금액
    inpt_dt: Optional[str] = None  # 입력일시