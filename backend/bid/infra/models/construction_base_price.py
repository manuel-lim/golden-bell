from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer
from backend.database import Base


"""
입찰공고목록 정보에 대한 공사기초금액조회 /getBidPblancListInfoCnstwkBsisAmount

검색조건에 기초금액 등록일시, 입찰공고번호를 입력하여 입찰공고번호, 입찰공고명, 기초금액, 기초금액공개일시, 
예비가격범위시작율, 평가기준금액, 난이도계수, 기타경비기준율 등의 공사의 기초금액정보 조회
"""
class ConstructionBasePrice(Base):
    __tablename__ = 'bid_construction_base_price'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    bid_ntce_nm = mapped_column(String(100), comment='입찰공고명')
    bssamt = mapped_column(String(21), comment='기초금액')
    bssamt_open_dt = mapped_column(String(19), comment='기초금액공개일시')
    rsrvtn_prce_rng_bgn_rate = mapped_column(String(7), comment='예비가격범위시작률')
    rsrvtn_prce_rng_end_rate = mapped_column(String(7), comment='예비가격범위종료율')
    evl_bss_amt = mapped_column(String(21), comment='평가기준금액')
    dfcltydgr_cfcnt = mapped_column(String(5), comment='난이도계수')
    etc_gnrlexpns_bss_rate = mapped_column(String(8), comment='기타경비기준율')
    gnrl_mngcst_bss_rate = mapped_column(String(8), comment='일반관리비기준율')
    prft_bss_rate = mapped_column(String(8), comment='이윤기준율')
    lbrcst_bss_rate = mapped_column(String(8), comment='노무비기준율')
    sfty_mngcst = mapped_column(String(17), comment='산업안전보건관리비')
    rtrfund_non = mapped_column(String(17), comment='퇴직공제부금비')
    env_cnsrvcst = mapped_column(String(15), comment='환경보전비')
    scontrct_payprce_pay_grnty_fee = mapped_column(String(21), comment='하도급대금지급보증수수료')
    mrfn_health_insrprm = mapped_column(String(18), comment='국민건강보험료')
    npn_insrprm = mapped_column(String(18), comment='국민연금보험료')
    rmrk1 = mapped_column(Text, comment='비고1')
    rmrk2 = mapped_column(Text, comment='비고2')
    odsn_lngtrmrcpr_insrprm = mapped_column(String(18), comment='노인장기요양보험료')
    useful_amt = mapped_column(String(21), comment='가용금액')
    inpt_dt = mapped_column(String(19), comment='입력일시')
    sfty_chck_mngcst = mapped_column(String(17), comment='안전관리비')
    bid_prce_calcl_a_yn = mapped_column(String(1), comment='입찰가격산식A여부')
    bss_amt_purcnstcst = mapped_column(String(22), comment='기초금액순공사비')
    qlty_mngcst = mapped_column(String(22), comment='품질관리비')
    qlty_mngcst_a_obj_yn = mapped_column(String(1), comment='품질관리비A적용대상여부')
