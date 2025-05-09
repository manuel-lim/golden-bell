from pydantic import BaseModel, Field
from typing import Optional

from backend.bid.domain.dto.bid_construction_dto import BidConstructionDTO
from backend.common import BidType
from backend.bid.domain import Bid
from backend.bid.domain.bid_construction import BidConstruction

class BidNoticeBody(BaseModel):
    from_bdgt_amt: Optional[str] = None  # 최소 예산금액
    to_bdgt_amt: Optional[str] = None  # 최대 예산금액

    bid_begin_dt: Optional[str] = None  # 입찰개시일시
    bid_clse_dt: Optional[str] = None  # 입찰마감일시

    bid_methd_nm: Optional[str] = None  # 입찰방식명
    bid_ntce_dt: Optional[str] = None  # 입찰공고일시

    bid_ntce_nm: Optional[str] = None  # 입찰공고명
    bid_ntce_no: Optional[str] = None  # 입찰공고번호

    ntce_instt_nm: Optional[str] = None  # 공고기관명
    openg_dt: Optional[str] = None  # 개찰일시
    presmpt_prce: Optional[str] = None  # 추정가격
    rgst_dt: Optional[str] = None  # 등록일시
    unty_ntce_no: Optional[str] = None  # 통합공고번호

    # bid_type: BidType = None  # 종류. 건설 / 외자 / 용역 / 물품
    page: Optional[str] = '1'
    per_page: Optional['int'] = '20'


class GetBidNoticeResponse(BaseModel):
    total_count: int
    data: Optional[list[Bid]] = None

class GetBidNoticeConstructionResponse(BaseModel):
    total_count: int
    data: Optional[list[BidConstructionDTO]] = None
