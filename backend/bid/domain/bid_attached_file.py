from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid

@dataclass
class BidAttachedFile(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    iss_dt: Optional[str] = None  # 교부일시
    bsns_div_nm: Optional[str] = None  # 업무구분명
    atch_sno: Optional[str] = None  # 첨부순번
    atch_doc_div_nm: Optional[str] = None  # 첨부문서구분명
    atch_file_nm: Optional[str] = None  # 첨부파일명
    atch_file_url: Optional[str] = None  # 첨부파일URL