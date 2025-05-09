from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column
from backend.database import Base

class WinBidRebid(Base):
    __tablename__ = 'win_bid_rebid'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    openg_rslt_div_nm = mapped_column(String(30), comment='개찰결과구분명')
    bid_ntce_no = mapped_column(String(11), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(3), comment='재입찰번호')
    bid_clse_dt = mapped_column(String(19), comment='입찰마감일시')
    openg_dt = mapped_column(String(19), comment='개찰일시')
    rbid_rsn = mapped_column(String(200), comment='재입찰사유')
    cmmn_spldmd_agrmnt_clse_dt = mapped_column(String(19), comment='공동수급혐정마감일시')