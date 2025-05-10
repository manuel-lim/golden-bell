from sqlalchemy.orm import mapped_column
from sqlalchemy import String, BigInteger, DateTime, text
from backend.database import Base


"""
개찰결과 개찰완료 목록 조회 /getOpengResultListInfoOpengCompt

물품, 공사, 용역, 외자의 개찰완료된 건에 대하여 최종낙찰업체 및 투찰업체의 개찰순위 정보를 제공하며 검색조건을 입찰공고번호하여 나라장터 개찰결과 
개찰완료 목록(개찰결과구분명, 입찰공고번호, 입찰공고차수, 입찰분류번호, 재입찰번호, 개찰순위, 최종낙찰업체사업자등록번호, 최종낙찰업체명, 최종낙찰업체대표자명, 
투찰금액, 투찰룰, 비고, 공종별입찰금액URL), 추첨번호1, 추첨번호2, 투찰일시 등 개찰완료 조회
"""

class OpenCompleted(Base):
    __tablename__ = 'win_bid_open_completed'
    __table_args__ = {'comment': '개찰결과 개찰완료 목록 조회'}

    id = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    openg_rslt_div_nm = mapped_column(String(30), comment='개찰결과구분명')
    bid_ntce_no = mapped_column(String(11), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(3), comment='재입찰번호')
    openg_rank = mapped_column(String(7), comment='개찰순위')
    prcbdr_bizno = mapped_column(String(10), comment='투찰업체사업자등록번호')
    prcbdr_nm = mapped_column(String(100), comment='투찰업체명')
    prcbdr_ceo_nm = mapped_column(String(35), comment='투찰업체대표자명')
    bidprc_amt = mapped_column(String(21), comment='투찰금액')
    bidprcrt = mapped_column(String(18), comment='투찰률')
    rmrk = mapped_column(String(200), comment='비고')
    cnstty_accot_bid_amt_url = mapped_column(String(150), comment='공종별입찰금액URL')
    drwt_no1 = mapped_column(String(3), comment='추첨번호1')
    drwt_no2 = mapped_column(String(3), comment='추첨번호2')
    bidprc_dt = mapped_column(String(19), comment='투찰일시')
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))