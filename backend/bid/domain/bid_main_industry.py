from typing import Optional
from backend.bid.domain import Bid


class BidNoticeDTO(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    bid_ntce_dt: Optional[str] = None  # 입찰공고일시
    cibl_apl_yn: Optional[str] = None  # 건산법적용여부
    cnstrt_wkara_mtlty_advc_psbl_yn: Optional[str] = None  # 건설업역상호진출가능여부
    cnstrt_wkrar_div_cd: Optional[str] = None  # 건설업역구분코드
    bidwinr_slctn_bss_cd: Optional[str] = None  # 낙찰자선정적용기준코드
    cnstty_ty_nm: Optional[str] = None  # 공종유형명
    tmp_nm: Optional[str] = None  # 공사대상업종명
    indstryty_mfrc_fld_nm: Optional[str] = None  # 업종주력분야명
    presmpt_amt: Optional[str] = None  # 추정금액
    presmpt_prce: Optional[str] = None  # 추정가격
    vat: Optional[str] = None  # 부가가치세
    evl_rt: Optional[str] = None  # 평가비율