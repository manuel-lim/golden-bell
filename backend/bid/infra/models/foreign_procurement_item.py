from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer

from backend.database import Base

"""
입찰공고목록 정보에 대한 외자 구매대상물품조회
"""

class ForeignProcurementItem(Base):
    __tablename__ = 'bid_foreign_procurement_item'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    prdct_sno = mapped_column(String(6), comment='물품순번')
    dminstt_cd = mapped_column(String(7), comment='수요기관코드')
    dminstt_nm = mapped_column(String(200), comment='수요기관명')
    hsk_no = mapped_column(String(10), comment='HSK번호')
    dtil_prdct_clsfc_no = mapped_column(String(10), comment='세부품명번호')
    dtil_prdct_clsfc_no_nm = mapped_column(String(200), comment='세부품명')
    qty = mapped_column(String(18), comment='수량')
    unit = mapped_column(String(30), comment='단위')
    asign_amt = mapped_column(String(18), comment='배정금액')
    asign_amt_crncy = mapped_column(String(3), comment='배정금액통화')
    ntce_ntice_dt = mapped_column(String(19), comment='공고게시일시')
    dlvry_cndtn_nm = mapped_column(String(50), comment='인도조건명')
    prdct_clsfc_no = mapped_column(String(50), comment='물품분류번호')
    prdct_clsfc_no_nm = mapped_column(String(50), comment='물품분류명')
    prdct_spec_nm = mapped_column(Text, comment='규격명')
    uprc = mapped_column(String(50), comment='단가')
    dlvr_tmlmt_dt = mapped_column(String(50), comment='납기일자')
    dlvr_daynum = mapped_column(String(50), comment='납기일수')
    dlvr_plce = mapped_column(String(50), comment='납품장소')