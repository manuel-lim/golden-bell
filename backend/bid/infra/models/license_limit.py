from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer
from backend.database import Base


"""
입찰공고목록 정보에 대한 면허제한정보조회 /getBidPblancListInfoLicenseLimit
검색조건에 등록일시범위(통합입찰공고)와 입찰공고번호를 입력하여 입찰공고번호, 입찰공고차수, 
제한그룹번호, 제한순번, 면허제한명, 허용업종목록, 등록일시를 포함한 면허제한정보 조회
"""
class LicenseLimit(Base):
    __tablename__ = 'bid_license_limit'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    lmt_grp_no = mapped_column(String(3), comment='제한그룹번호')
    lmt_sno = mapped_column(String(6), comment='제한순번')
    lcns_lmt_nm = mapped_column(String(200), comment='면허제한명')
    permsn_indstryty_list = mapped_column(Text, comment='허용업종목록')
    rgst_dt = mapped_column(String(19), comment='등록일시')
    bsns_div_nm = mapped_column(String(30), comment='업무구분명')
    indstryty_mfrc_fld_list = mapped_column(Text, comment='주력업종분야목록')