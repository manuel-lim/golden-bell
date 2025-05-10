from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer
from backend.database import Base


"""
검색조건에 등록일시와 입찰공고번호를 입력하여 입찰 평가대상주력분야의 건산법적용여부, 건설업역상호진출가능여부, 건설업역구분코드, 낙찰자선정적용기준코드, 
공종유형명, 공사대상업종명, 업종주력분야명, 추정금액, 추정가격, 부가가치세, 평가비율을 조회
"""
class MainIndustry(Base):
    __tablename__ = 'bid_main_industry'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_ntce_dt = mapped_column(String(30), comment='입찰공고일시')
    cibl_apl_yn = mapped_column(String(1), comment='건산법적용여부')
    cnstrt_wkara_mtlty_advc_psbl_yn = mapped_column(String(1), comment='건설업역상호진출가능여부')
    cnstrt_wkrar_div_cd = mapped_column(String(9), comment='건설업역구분코드')
    bidwinr_slctn_bss_cd = mapped_column(String(9), comment='낙찰자선정적용기준코드')
    cnstty_ty_nm = mapped_column(String(30), comment='공종유형명')
    tmp_nm = mapped_column(Text, comment='공사대상업종명')
    indstryty_mfrc_fld_nm = mapped_column(Text, comment='업종주력분야명')
    presmpt_amt = mapped_column(String(22), comment='추정금액')
    presmpt_prce = mapped_column(String(22), comment='추정가격')
    vat = mapped_column(String(22), comment='부가가치세')
    evl_rt = mapped_column(String(6), comment='평가비율')
