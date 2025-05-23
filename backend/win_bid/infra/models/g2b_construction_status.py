from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer
from backend.database import Base


"""
나라장터 검색조건에 의한 낙찰된 목록 현황 공사조회 /getScsbidListSttusCnstwkPPSSrch

검색조건을 공고일시, 개찰일시, 입찰공고번호, 입찰공고명, 공고기관코드, 공고기관명, 수요기관코드, 수요기관명, 참조번호, 참가제한지역코드, 참가제한지역명, 
업종코드, 업종명, 추정가격시작, 추정가격종료, 세부품명번호, 다수공급경쟁자여부, 조달요청번호, 국제구분코드로 공사에대한 나라장터 최종낙찰자 목록(입찰공고번호,
입찰공고명, 참가업체수, 최종낙찰업체명, 사업자번호, 최종낙찰률, 실개찰일시, 수요기관)을 조회
"""


class G2BConstructionStatus(Base):
    __tablename__ = 'win_bid_g2b_construction_status'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(3), comment='재입찰번호')
    ntce_div_cd = mapped_column(String(9), comment='공고구분코드')
    bid_ntce_nm = mapped_column(String(100), comment='입찰공고명')
    prtcpt_cnum = mapped_column(String(6), comment='참가업체수')
    bidwinnr_nm = mapped_column(String(100), comment='최종낙찰업체명')
    bidwinnr_bizno = mapped_column(String(10), comment='최종낙찰업체사업자등록번호')
    bidwinnr_ceo_nm = mapped_column(String(35), comment='최종낙찰업체대표자명')
    bidwinnr_adrs = mapped_column(String(200), comment='최종낙찰업체주소')
    bidwinnr_tel_no = mapped_column(String(25), comment='최종낙찰업체전화번호')
    sucsfbid_amt = mapped_column(String(21), comment='최종낙찰금액')
    sucsfbid_rate = mapped_column(String(18), comment='최종낙찰률')
    rl_openg_dt = mapped_column(String(19), comment='실개찰일시')
    dminstt_cd = mapped_column(String(7), comment='수요기관코드')
    dminstt_nm = mapped_column(String(200), comment='수요기관명')
    rgst_dt = mapped_column(String(19), comment='등록일시')
    fnl_sucsf_date = mapped_column(String(10), comment='최종낙찰일자')
    fnl_sucsf_corp_ofcl = mapped_column(String(35), comment='최종낙찰업체담당자')