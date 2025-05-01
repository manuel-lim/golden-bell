from typing import Optional
from dataclasses import dataclass

from backend.bid.domain import Bid


@dataclass
class BidAttachedEFile(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    atch_sno: Optional[str] = None  # 첨부순번
    eorder_doc_div_nm: Optional[str] = None  # e발주문서구분명
    eorder_atch_file_nm: Optional[str] = None  # e발주첨부파일명
    eorder_atch_file_url: Optional[str] = None  # e발주첨부파일URL