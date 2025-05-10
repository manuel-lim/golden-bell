from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer
from backend.database import Base


"""
첨부파일정보조회
낙찰자결정방법이 [경쟁적 대화에 의한 낙찰자 선정 낙찰방법] 일경우 검색조건에 등록일시, 입찰공고번호, 교부일시를 입력하여 혁신장터에서 교부된 최종제안요청서 첨부파일정보를 조회함
"""

class AttachedFile(Base):
    __tablename__ = 'bid_attached_file'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    iss_dt = mapped_column(String(19), comment='교부일시')
    bsns_div_nm = mapped_column(String(30), comment='업무구분명')
    atch_sno = mapped_column(String(7), comment='첨부순번')
    atch_doc_div_nm = mapped_column(String(50), comment='첨부문서구분명')
    atch_file_nm = mapped_column(String(200), comment='첨부파일명')
    atch_file_url = mapped_column(Text, comment='첨부파일URL')
