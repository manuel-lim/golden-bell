from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer
from backend.database import Base


"""
입찰공고목록 정보에 대한 기타공고조회 /getBidPblancListInfoEtc
검색조건에 등록일시, 입찰공고번호를 입력하여 나라장터의 입찰공고번호, 공고명, 발주기관, 수요기관, 계약체결방법명 등 기타공고정보를 조회
"""

class Etc(Base):
    __tablename__ = 'bid_etc'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    rgst_ty_nm = mapped_column(String(100), comment='등록유형명')
    ntce_kind_nm = mapped_column(String(100), comment='공고종류명')
    bid_ntce_dt = mapped_column(String(30), comment='입찰공고일시')
    ref_no = mapped_column(String(105), comment='참조번호')
    bid_ntce_nm = mapped_column(String(100), comment='입찰공고명')
    ntce_instt_cd = mapped_column(String(7), comment='공고기관코드')
    ntce_instt_nm = mapped_column(String(200), comment='공고기관명')
    dminstt_nm = mapped_column(String(200), comment='수요기관명')
    bid_methd_nm = mapped_column(String(200), comment='입찰방식명')
    cntrct_cncls_mthd_nm = mapped_column(String(200), comment='계약체결방법명')
    bid_begin_dt = mapped_column(String(19), comment='입찰개시일시')
    bid_clse_dt = mapped_column(String(19), comment='입찰마감일시')
    openg_dt = mapped_column(String(19), comment='개찰일시')
    ntce_spec_doc_url1 = mapped_column(Text, comment='공고규격서URL1')
    ntce_spec_doc_url2 = mapped_column(Text, comment='공고규격서URL2')
    ntce_spec_doc_url3 = mapped_column(Text, comment='공고규격서URL3')
    ntce_spec_doc_url4 = mapped_column(Text, comment='공고규격서URL4')
    ntce_spec_doc_url5 = mapped_column(Text, comment='공고규격서URL5')
    ntce_spec_file_nm1 = mapped_column(String(256), comment='공고규격파일명1')
    ntce_spec_file_nm2 = mapped_column(String(256), comment='공고규격파일명2')
    ntce_spec_file_nm3 = mapped_column(String(256), comment='공고규격파일명3')
    ntce_spec_file_nm4 = mapped_column(String(256), comment='공고규격파일명4')
    ntce_spec_file_nm5 = mapped_column(String(256), comment='공고규격파일명5')
    rbid_permsn_yn = mapped_column(String(1), comment='재입찰허용여부')
    presmpt_prce = mapped_column(String(25), comment='추정가격')
    openg_plce = mapped_column(String(100), comment='개찰장소')
    bid_ntce_dtl_url = mapped_column(Text, comment='입찰공고상세URL')
    bid_ntce_url = mapped_column(Text, comment='입찰공고URL')
    bid_prtcpt_fee = mapped_column(String(21), comment='입찰참가수수료')
    bid_prtcpt_fee_paymnt_yn = mapped_column(String(30), comment='입찰보증금납부대상여부')
    unty_ntce_no = mapped_column(String(50), comment='통합공고번호')
    cmmn_spldmd_yn = mapped_column(String(1), comment='공동수급여부')
    bid_qlfct_rgst_cntnts = mapped_column(Text, comment='입찰참가자격내용')
    rgst_dt = mapped_column(String(19), comment='등록일시')
    sucsfbid_mthd_nm = mapped_column(String(200), comment='낙찰방법명')
    rmrk_cntnts = mapped_column(Text, comment='비고내용')
    bid_grntymny_paymnt_obj_yn = mapped_column(String(1), comment='')
