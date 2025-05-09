from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer
from backend.database import Base


class WinBidFail(Base):
    __tablename__ = 'win_bid_fail'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    openg_rslt_div_nm = mapped_column(String(30), comment='개찰결과구분명')
    bid_ntce_no = mapped_column(String(11), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(3), comment='재입찰번호')
    nobid_rsn = mapped_column(String(200), comment='유찰사유')