from dataclasses import dataclass
from typing import Optional
from backend.bid.domain import Bid


"""
검색조건에 등록일시, 입찰공고번호, 변경일시를 입력하여 
나라장터의 입찰공고번호, 공고명, 발주기관, 수요기관, 계약체결방법명 등 외자부분의 입찰공고정보를 조회함
"""
@dataclass
class ForeignProcurement(Bid):
    bid_ntce_no: Optional[str] = None  # 입찰공고번호
    bid_ntce_ord: Optional[str] = None  # 입찰공고차수
    re_ntce_yn: Optional[str] = None  # 재공고여부
    rgst_ty_nm: Optional[str] = None  # 등록유형명
    ntce_kind_nm: Optional[str] = None  # 공고종류명
    intrbid_yn: Optional[str] = None  # 국제입찰여부
    bid_ntce_dt: Optional[str] = None  # 입찰공고일시
    ref_no: Optional[str] = None  # 참조번호
    bid_ntce_nm: Optional[str] = None  # 입찰공고명
    ntce_instt_cd: Optional[str] = None  # 공고기관코드
    ntce_instt_nm: Optional[str] = None  # 공고기관명
    dminstt_cd: Optional[str] = None  # 수요기관코드
    dminstt_nm: Optional[str] = None  # 수요기관명
    bid_methd_nm: Optional[str] = None  # 입찰방식명
    cntrct_cncls_mthd_nm: Optional[str] = None  # 계약체결방법명
    ntce_instt_ofcl_nm: Optional[str] = None  # 공고기관담당자명
    ntce_instt_ofcl_tel_no: Optional[str] = None  # 공고기관담당자전화번호
    ntce_instt_ofcl_email_adrs: Optional[str] = None  # 공고기관담당자이메일주소
    exctv_nm: Optional[str] = None  # 집행관명
    bid_qlfct_rgst_dt: Optional[str] = None  # 입찰참가자격등록마감일시
    cmmn_spldmd_agrmnt_rcptdoc_methd: Optional[str] = None  # 공동수급협정서접수방식
    cmmn_spldmd_agrmnt_clse_dt: Optional[str] = None  # 공동수급협정마감일시
    cmmn_spldmd_corp_rgn_lmt_yn: Optional[str] = None  # 공동수급업체지역제한여부
    bid_begin_dt: Optional[str] = None  # 입찰개시일시
    bid_clse_dt: Optional[str] = None  # 입찰마감일시
    openg_dt: Optional[str] = None  # 개찰일시
    ntce_spec_doc_url1: Optional[str] = None  # 공고규격서URL1
    ntce_spec_doc_url2: Optional[str] = None  # 공고규격서URL2
    ntce_spec_doc_url3: Optional[str] = None  # 공고규격서URL3
    ntce_spec_doc_url4: Optional[str] = None  # 공고규격서URL4
    ntce_spec_doc_url5: Optional[str] = None  # 공고규격서URL5
    ntce_spec_doc_url6: Optional[str] = None  # 공고규격서URL6
    ntce_spec_doc_url7: Optional[str] = None  # 공고규격서URL7
    ntce_spec_doc_url8: Optional[str] = None  # 공고규격서URL8
    ntce_spec_doc_url9: Optional[str] = None  # 공고규격서URL9
    ntce_spec_doc_url10: Optional[str] = None  # 공고규격서URL10
    ntce_spec_file_nm1: Optional[str] = None  # 공고규격파일명1
    ntce_spec_file_nm2: Optional[str] = None  # 공고규격파일명2
    ntce_spec_file_nm3: Optional[str] = None  # 공고규격파일명3
    ntce_spec_file_nm4: Optional[str] = None  # 공고규격파일명4
    ntce_spec_file_nm5: Optional[str] = None  # 공고규격파일명5
    ntce_spec_file_nm6: Optional[str] = None  # 공고규격파일명6
    ntce_spec_file_nm7: Optional[str] = None  # 공고규격파일명7
    ntce_spec_file_nm8: Optional[str] = None  # 공고규격파일명8
    ntce_spec_file_nm9: Optional[str] = None  # 공고규격파일명9
    ntce_spec_file_nm10: Optional[str] = None  # 공고규격파일명10
    rbid_permsn_yn: Optional[str] = None  # 재입찰허용여부
    prdct_clsfc_lmt_yn: Optional[str] = None  # 물품분류제한여부
    mnfct_yn: Optional[str] = None  # 제조여부
    prearng_prce_dcsn_mthd_nm: Optional[str] = None  # 예정가격결정방법명
    tot_prdprc_num: Optional[str] = None  # 총예가건수
    drwt_prdprc_num: Optional[str] = None  # 추첨예가건수
    asign_bdgt_amt: Optional[str] = None  # 배정예산금액
    presmpt_prce: Optional[str] = None  # 추정가격
    openg_plce: Optional[str] = None  # 개찰장소
    bid_ntce_dtl_url: Optional[str] = None  # 입찰공고상세URL
    bid_ntce_url: Optional[str] = None  # 입찰공고URL
    bid_prtcpt_fee_paymnt_yn: Optional[str] = None  # 입찰참가수수료납부여부
    bid_prtcpt_fee: Optional[str] = None  # 입찰참가수수료
    bid_grntymny_paymnt_yn: Optional[str] = None  # 입찰보증금납부여부
    crdtr_nm: Optional[str] = None  # 채권자명
    prdct_sno: Optional[str] = None  # 물품순번
    dtil_prdct_clsfc_no: Optional[str] = None  # 세부품명번호
    dtil_prdct_clsfc_no_nm: Optional[str] = None  # 세부품명
    prdct_spec_nm: Optional[str] = None  # 물품규격명
    prdct_qty: Optional[str] = None  # 물품수량
    prdct_unit: Optional[str] = None  # 물품단위
    prdct_uprc: Optional[str] = None  # 물품단가
    dlvr_tmlmt_dt: Optional[str] = None  # 납품기한일시
    dlvr_daynum: Optional[str] = None  # 납품일수
    dlvry_cndtn_nm: Optional[str] = None  # 인도조건명
    purchs_obj_prdct_list: Optional[str] = None  # 구매대상물품목록
    unty_ntce_no: Optional[str] = None  # 통합공고번호
    cmmn_spldmd_methd_cd: Optional[str] = None  # 공동수급방식코드
    cmmn_spldmd_methd_nm: Optional[str] = None  # 공동수급방식명
    std_ntce_doc_url: Optional[str] = None  # 표준공고서URL
    brffc_bidprc_permsn_yn: Optional[str] = None  # 지사투찰허용여부
    dsgnt_cmpt_yn: Optional[str] = None  # 지명경쟁여부
    rsrvtn_prce_re_mkng_mthd_nm: Optional[str] = None  # 예비가격재작성방법명
    arslt_appl_doc_rcpt_mthd_nm: Optional[str] = None  # 실적신청서접수방법명
    arslt_appl_doc_rcpt_dt: Optional[str] = None  # 실적신청서접수일시
    order_plan_unty_no: Optional[str] = None  # 발주계획통합번호
    sucsfbid_lwlt_rate: Optional[str] = None  # 낙찰하한율
    rgst_dt: Optional[str] = None  # 등록일시
    bf_spec_rgst_no: Optional[str] = None  # 사전규격등록번호
    sucsfbid_mthd_cd: Optional[str] = None  # 낙찰방법코드
    sucsfbid_mthd_nm: Optional[str] = None  # 낙찰방법명
    chg_dt: Optional[str] = None  # 변경일시
    dminstt_ofcl_email_adrs: Optional[str] = None  # 수요기관담당자이메일주소
    indstryty_lmt_yn: Optional[str] = None  # 업종제한여부
    chg_ntce_rsn: Optional[str] = None  # 변경공고사유
    rbid_openg_dt: Optional[str] = None  # 재입찰개찰일시
    bid_wgrntee_rcpt_clse_dt: Optional[str] = None  # 입찰보증서접수마감일시