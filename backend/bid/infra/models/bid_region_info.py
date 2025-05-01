from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text
from backend.database import Base


# 참가가능지역정보조회
class BidRegionInfo(Base):
    __tablename__ = 'bid_region_info'

    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    lmt_sno = mapped_column(String(6), comment='제한순번')
    prtcpt_psbl_rgn_nm = mapped_column(String(100), comment='참가가능지역명')
    rgst_dt = mapped_column(String(19), comment='등록일시')
    bsns_div_nm = mapped_column(String(30), comment='업무구분명')
