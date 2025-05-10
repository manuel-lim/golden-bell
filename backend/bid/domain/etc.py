from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


"""
검색조건에 등록일시, 입찰공고번호를 입력하여 나라장터의 입찰공고번호, 공고명, 발주기관, 수요기관, 계약체결방법명 등 기타공고정보를 조회
"""
@dataclass
class Etc(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    rgst_ty_nm: Optional[str] = None  # 등록유형명
    ntce_kind_nm: Optional[str] = None  # 공고종류명
    bid_ntce_dt: Optional[str] = None  # 입찰공고일시
    ref_no: Optional[str] = None  # 참조번호
    bid_ntce_nm: Optional[str] = None  # 입찰공고명
    ntce_instt_cd: Optional[str] = None  # 공고기관코드
    ntce_instt_nm: Optional[str] = None  # 공고기관명
    dminstt_nm: Optional[str] = None  # 수요기관명
    bid_methd_nm: Optional[str] = None  # 입찰방식명
    cntrct_cncls_mthd_nm: Optional[str] = None  # 계약체결방법명
    bid_begin_dt: Optional[str] = None  # 입찰개시일시
    bid_clse_dt: Optional[str] = None  # 입찰마감일시
    openg_dt: Optional[str] = None  # 개찰일시
    ntce_spec_doc_url1: Optional[str] = None  # 공고규격서URL1
    ntce_spec_doc_url2: Optional[str] = None  # 공고규격서URL2
    ntce_spec_doc_url3: Optional[str] = None  # 공고규격서URL3
    ntce_spec_doc_url4: Optional[str] = None  # 공고규격서URL4
    ntce_spec_doc_url5: Optional[str] = None  # 공고규격서URL5
    ntce_spec_file_nm1: Optional[str] = None  # 공고규격파일명1
    ntce_spec_file_nm2: Optional[str] = None  # 공고규격파일명2
    ntce_spec_file_nm3: Optional[str] = None  # 공고규격파일명3
    ntce_spec_file_nm4: Optional[str] = None  # 공고규격파일명4
    ntce_spec_file_nm5: Optional[str] = None  # 공고규격파일명5
    rbid_permsn_yn: Optional[str] = None  # 재입찰허용여부
    presmpt_prce: Optional[str] = None  # 추정가격
    openg_plce: Optional[str] = None  # 개찰장소
    bid_ntce_dtl_url: Optional[str] = None  # 입찰공고상세URL
    bid_ntce_url: Optional[str] = None  # 입찰공고URL
    bid_prtcpt_fee: Optional[str] = None  # 입찰참가수수료
    bid_prtcpt_fee_paymnt_yn: Optional[str] = None  # 입찰보증금납부대상여부
    unty_ntce_no: Optional[str] = None  # 통합공고번호
    cmmn_spldmd_yn: Optional[str] = None  # 공동수급여부
    bid_qlfct_rgst_cntnts: Optional[str] = None  # 입찰참가자격내용
    rgst_dt: Optional[str] = None  # 등록일시
    sucsfbid_mthd_nm: Optional[str] = None  # 낙찰방법명
    rmrk_cntnts: Optional[str] = None  # 비고내용
    bid_grntymny_paymnt_obj_yn: Optional[str] = None