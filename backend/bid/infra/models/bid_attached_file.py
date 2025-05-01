from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text
from backend.database import Base


class BidAttachedFile(Base):
    __tablename__ = 'bid_attached_file'

    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    iss_dt = mapped_column(String(19), comment='교부일시')
    bsns_div_nm = mapped_column(String(30), comment='업무구분명')
    atch_sno = mapped_column(String(7), comment='첨부순번')
    atch_doc_div_nm = mapped_column(String(50), comment='첨부문서구분명')
    atch_file_nm = mapped_column(String(200), comment='첨부파일명')
    atch_file_url = mapped_column(Text, comment='첨부파일URL')
