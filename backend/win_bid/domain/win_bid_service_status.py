from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class WinBidServiceStatusModel(BaseModel):
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    bid_clsfc_no: Optional[str] = None
    rbid_no: Optional[str] = None
    ntce_div_cd: Optional[str] = None
    bid_ntce_nm: Optional[str] = None
    prtcpt_cnum: Optional[str] = None
    bidwinnr_nm: Optional[str] = None
    bidwinnr_bizno: Optional[str] = None
    bidwinnr_ceo_nm: Optional[str] = None
    bidwinnr_adrs: Optional[str] = None
    bidwinnr_tel_no: Optional[str] = None
    sucsfbid_amt: Optional[str] = None
    sucsfbid_rate: Optional[str] = None
    rl_openg_dt: Optional[str] = None
    dminstt_cd: Optional[str] = None
    dminstt_nm: Optional[str] = None
    rgst_dt: Optional[str] = None
    fnl_sucsf_date: Optional[str] = None
    fnl_sucsf_corp_ofcl: Optional[str] = None
    created_at: Optional[str] = None