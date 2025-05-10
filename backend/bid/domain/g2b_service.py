from dataclasses import dataclass
from typing import Optional
from backend.bid.domain.service import Service


"""
나라장터검색조건에 의한 입찰공고용역조회 /getBidPblancListInfoServcPPSSrch
 
검색조건에 공고게시일시, 개찰일시 범위, 공고기관, 수요기관, 참조번호 등을 입력하여 
나라장터의 입찰공고번호, 공고명, 발주기관, 수요기관, 계약체결방법명 등 용역부분의 입찰공고정보를 조회함
"""
@dataclass
class BidG2BService(Service):
    pass
