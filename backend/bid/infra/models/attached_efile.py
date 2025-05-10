from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer
from backend.database import Base

"""
입찰공고목록 정보에 대한 e발주 첨부파일정보조회
검색조건에 등록일시범위(통합입찰공고)와 입찰공고번호를 입력하여 입찰공고번호, 입찰공고차수, 첨부순번, e발주문서구분명, e발주첨부파일명, e발주첨부파일URL 정보 조회
"""

class AttachedEFile(Base):
    __tablename__ = 'bid_attached_efile'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    atch_sno = mapped_column(String(7), comment='첨부순번')
    eorder_doc_div_nm = mapped_column(String(50), comment='e발주문서구분명')
    eorder_atch_file_nm = mapped_column(String(200), comment='e발주첨부파일명')
    eorder_atch_file_url = mapped_column(Text, comment='e발주첨부파일URL')
