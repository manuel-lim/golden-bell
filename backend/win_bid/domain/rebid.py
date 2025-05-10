from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class Rebid(BaseModel):
    openg_rslt_div_nm: Optional[str] = None
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    bid_clsfc_no: Optional[str] = None
    rbid_no: Optional[str] = None
    bid_clse_dt: Optional[str] = None
    openg_dt: Optional[str] = None
    rbid_rsn: Optional[str] = None
    cmmn_spldmd_agrmnt_clse_dt: Optional[str] = None