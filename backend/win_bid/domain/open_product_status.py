from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class ProductStatus(BaseModel):
    id: Optional[int] = None
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    bid_clsfc_no: Optional[str] = None
    rbid_no: Optional[str] = None
    bid_ntce_nm: Optional[str] = None
    openg_dt: Optional[str] = None
    prtcpt_cnum: Optional[str] = None
    openg_corp_info: Optional[str] = None
    progrs_div_cd_nm: Optional[str] = None
    inpt_dt: Optional[str] = None
    rsrvtn_prce_file_existnce_yn: Optional[str] = None
    ntce_instt_cd: Optional[str] = None
    ntce_instt_nm: Optional[str] = None
    dminstt_cd: Optional[str] = None
    dminstt_nm: Optional[str] = None
    openg_rslt_ntc_cntnts: Optional[str] = None
    created_at: Optional[str] = None
