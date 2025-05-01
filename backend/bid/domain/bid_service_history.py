from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


# 용역변경이력조회
@dataclass
class G2BServiceChangeHistoryDTO(Bid):
    bsns_div_nm: Optional[str] = None  # 업무구분명
    chg_data_div_nm: Optional[str] = None  # 변경데이터구분명
    chg_dt: Optional[str] = None  # 변경일시
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_clsfc_no: Optional[str] = None  # 입찰분류번호
    rbid_no: Optional[str] = None  # 재입찰번호
    chg_item_nm: Optional[str] = None  # 변경항목명
    bfchg_val: Optional[str] = None  # 변경전값
    afchg_val: Optional[str] = None  # 변경후값
    lcns_lmt_cd_rgst_list: Optional[str] = None  # 면허제한코드변경후목록
