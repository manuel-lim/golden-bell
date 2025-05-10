from typing import Optional
from dataclasses import dataclass
from backend.bid.domain import Bid

"""
입찰공고목록 정보에 대한 e발주 첨부파일정보조회 /getBidPblancListInfoEorderAtchFileInfo

검색조건에 등록일시범위(통합입찰공고)와 입찰공고번호를 입력하여 입찰공고번호, 입찰공고차수, 첨부순번, e발주문서구분명, e발주첨부파일명, e발주첨부파일URL 정보 조회
"""

@dataclass
class AttachedEFile(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    atch_sno: Optional[str] = None  # 첨부순번
    eorder_doc_div_nm: Optional[str] = None  # e발주문서구분명
    eorder_atch_file_nm: Optional[str] = None  # e발주첨부파일명
    eorder_atch_file_url: Optional[str] = None  # e발주첨부파일URL
