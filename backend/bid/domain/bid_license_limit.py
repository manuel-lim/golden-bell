from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text
from backend.database import Base


# 면허제한정보조회
class BidLicenseLimit(Base):
    __tablename__ = 'bid_license_limit'

    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    lmt_grp_no = mapped_column(String(3), comment='제한그룹번호')
    lmt_sno = mapped_column(String(6), comment='제한순번')
    lcns_lmt_nm = mapped_column(String(200), comment='면허제한명')
    permsn_indstryty_list = mapped_column(Text, comment='허용업종목록')
    rgst_dt = mapped_column(String(19), comment='등록일시')
    bsns_div_nm = mapped_column(String(30), comment='업무구분명')
    indstryty_mfrc_fld_list = mapped_column(Text, comment='주력업종분야목록')
