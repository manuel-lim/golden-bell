from sqlalchemy.orm import mapped_column
from sqlalchemy import String, BigInteger, DateTime, text
from backend.database import Base

"""
개찰결과 외자 목록 조회 /getOpengResultListInfoFrgcpt

유찰, 개찰완료, 재입찰건에 대한 개찰결과를 제공하며 검색조건을 입력일시, 공고일시, 개찰일시, 입찰공고번호로하여 외자에 대한 나라장터 개찰결과 
목록(입찰공고번호, 입찰공고명, 개찰일시, 참가업체수, 개찰업체정보, 진행구분코드명, 입력일시, 예비가격파일존재여부, 공고기관명, 수요기관명)을 조회
"""

class OpenForeignProcurementStatus(Base):
    __tablename__ = 'win_bid_open_foreign_procurement_status'
    __table_args__ = {'comment': '개찰결과 외자 목록 조회'}

    id = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(11), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(3), comment='재입찰번호')
    bid_ntce_nm = mapped_column(String(100), comment='입찰공고명')
    openg_dt = mapped_column(String(19), comment='개찰일시')
    prtcpt_cnum = mapped_column(String(6), comment='참가업체수')
    openg_corp_info = mapped_column(String(500), comment='개찰업체정보')
    progrs_div_cd_nm = mapped_column(String(4), comment='진행구분코드명')
    inpt_dt = mapped_column(String(19), comment='입력일시')
    rsrvtn_prce_file_existnce_yn = mapped_column(String(1), comment='예비가격파일존재여부')
    ntce_instt_cd = mapped_column(String(7), comment='공고기관코드')
    ntce_instt_nm = mapped_column(String(200), comment='공고기관명')
    dminstt_cd = mapped_column(String(7), comment='수요기관코드')
    dminstt_nm = mapped_column(String(200), comment='수요기관명')
    openg_rslt_ntc_cntnts = mapped_column(String(4000), comment='개찰결과공지내용')
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))