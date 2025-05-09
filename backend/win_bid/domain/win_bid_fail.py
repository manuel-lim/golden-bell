from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class WinBidFailModel(BaseModel):
    openg_rslt_div_nm: Optional[str] = None
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    bid_clsfc_no: Optional[str] = None
    rbid_no: Optional[str] = None
    nobid_rsn: Optional[str] = None
