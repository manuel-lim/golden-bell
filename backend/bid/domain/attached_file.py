from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


"""
첨부파일정보조회
낙찰자결정방법이 [경쟁적 대화에 의한 낙찰자 선정 낙찰방법] 일경우 검색조건에 등록일시, 입찰공고번호, 교부일시를 입력하여 혁신장터에서 교부된 최종제안요청서 첨부파일정보를 조회함
"""
@dataclass
class AttachedFile(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    iss_dt: Optional[str] = None  # 교부일시
    bsns_div_nm: Optional[str] = None  # 업무구분명
    atch_sno: Optional[str] = None  # 첨부순번
    atch_doc_div_nm: Optional[str] = None  # 첨부문서구분명
    atch_file_nm: Optional[str] = None  # 첨부파일명
    atch_file_url: Optional[str] = None  # 첨부파일URL
