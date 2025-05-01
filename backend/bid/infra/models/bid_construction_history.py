from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text
from backend.database import Base


# 공사변경이력조회
class BidConstructionHistory(Base):
    __tablename__ = 'bid_construction_history'

    bsns_div_nm = mapped_column(String(30), comment='업무구분명')
    chg_data_div_nm = mapped_column(String(30), comment='변경데이터구분명')
    chg_dt = mapped_column(String(19), comment='변경일시')
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(11), comment='재입찰번호')
    chg_item_nm = mapped_column(String(200), comment='변경항목명')
    bfchg_val = mapped_column(Text, comment='변경전값')
    afchg_val = mapped_column(Text, comment='변경후값')
    lcns_lmt_cd_rgst_list = mapped_column(Text, comment='면허제한코드변경후목록')
