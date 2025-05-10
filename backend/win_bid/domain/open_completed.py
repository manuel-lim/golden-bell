from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass


@dataclass
class OpenCompleted(BaseModel):
    id: Optional[int] = None
    openg_rslt_div_nm: Optional[str] = None
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    bid_clsfc_no: Optional[str] = None
    rbid_no: Optional[str] = None
    openg_rank: Optional[str] = None
    prcbdr_bizno: Optional[str] = None
    prcbdr_nm: Optional[str] = None
    prcbdr_ceo_nm: Optional[str] = None
    bidprc_amt: Optional[str] = None
    bidprcrt: Optional[str] = None
    rmrk: Optional[str] = None
    cnstty_accot_bid_amt_url: Optional[str] = None
    drwt_no1: Optional[str] = None
    drwt_no2: Optional[str] = None
    bidprc_dt: Optional[str] = None
    created_at: Optional[str] = None