from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass


@dataclass
class OpenProductPrice(BaseModel):

    id: Optional[int] = None
    bid_ntce_no: Optional[str] = None
    bid_ntce_ord: Optional[str] = None
    bid_clsfc_no: Optional[str] = None
    rbid_no: Optional[str] = None
    bid_ntce_nm: Optional[str] = None
    plnprc: Optional[str] = None
    bssamt: Optional[str] = None
    tot_rsrvtn_prce_num: Optional[str] = None
    compno_rsrvtn_prce_sno: Optional[str] = None
    bsis_plnprc: Optional[str] = None
    drwt_yn: Optional[str] = None
    drwt_num: Optional[str] = None
    bidwinr_slctn_apl_bss_cntnts: Optional[str] = None
    rl_openg_dt: Optional[str] = None
    bssamt_bss_up_num: Optional[str] = None
    compno_rsrvtn_prce_mkng_dt: Optional[str] = None
    inpt_dt: Optional[str] = None
    prearng_prce_purcnstcst: Optional[str] = None
    created_at: Optional[str] = None