from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text

from backend.database import Base


class BidAttachedEFile(Base):
    __tablename__ = 'bid_attached_efile'

    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    atch_sno = mapped_column(String(7), comment='첨부순번')
    eorder_doc_div_nm = mapped_column(String(50), comment='e발주문서구분명')
    eorder_atch_file_nm = mapped_column(String(200), comment='e발주첨부파일명')
    eorder_atch_file_url = mapped_column(Text, comment='e발주첨부파일URL')
