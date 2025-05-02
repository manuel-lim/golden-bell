from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text
from backend.database import Base


"""
검색조건에 등록일시범위(통합입찰공고)와 입찰공고번호를 입력하여 입찰공고번호, 
입찰공고차수, 입찰분류번호, 물품순번, 수요기관코드, 수요기관명, 물품분류번호, 
품명, 세부품명번호, 세부품명, 수량, 단위, 단가, 납품기한일시, 납품일수, 납품장소, 인도조건명 등 용역 구매대상물품 정보 조회
"""
class BidServiceProcurementItem(Base):
    __tablename__ = 'bid_service_procurement_item'

    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    prdct_sno = mapped_column(String(6), comment='물품순번')
    dminstt_cd = mapped_column(String(7), comment='수요기관코드')
    dminstt_nm = mapped_column(String(200), comment='수요기관명')
    prdct_clsfc_no = mapped_column(String(8), comment='물품분류번호')
    prdct_clsfc_no_nm = mapped_column(String(200), comment='품명')
    dtil_prdct_clsfc_no = mapped_column(String(10), comment='세부품명번호')
    dtil_prdct_clsfc_no_nm = mapped_column(String(200), comment='세부품명')
    prdct_spec_nm = mapped_column(String(200), comment='물품규격명')
    qty = mapped_column(String(18), comment='수량')
    unit = mapped_column(String(30), comment='단위')
    uprc = mapped_column(String(18), comment='단가')
    dlvr_tmlmt_dt = mapped_column(String(19), comment='납품기한일시')
    dlvr_daynum = mapped_column(String(5), comment='납품일수')
    dlvr_plce = mapped_column(String(256), comment='납품장소')
    dlvry_cndtn_nm = mapped_column(String(100), comment='인도조건명')
    ntce_ntice_dt = mapped_column(String(19), comment='공고게시일시')
