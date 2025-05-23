from dataclasses import dataclass
from backend.bid.domain.construction import Construction


"""
나라장터검색조건에 의한 입찰공고공사조회 / getBidPblancListInfoCnstwkPPSSrch

검색조건에 공고게시일시, 개찰일시 범위, 공고기관, 수요기관, 참조번호 등을 입력하여 
나라장터의 입찰공고번호, 공고명, 발주기관, 수요기관, 계약체결방법명 등 공사부분의 입찰공고정보를 조회함
"""
@dataclass
class G2BConstruction(Construction):
    pass