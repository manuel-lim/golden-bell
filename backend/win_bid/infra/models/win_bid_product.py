from sqlalchemy import Column, String, Integer
from backend.database import Base


class WinBidProduct(Base):
    __tablename__ = 'win_bid_product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bid_ntce_no = Column(String(40), comment="입찰공고번호")
    bid_ntce_ord = Column(String(3), comment="입찰공고차수")
    bid_clsfc_no = Column(String(5), comment="입찰분류번호")
    rbid_no = Column(String(3), comment="재입찰번호")
    ntce_div_cd = Column(String(9), comment="공고구분코드")
    bid_ntce_nm = Column(String(100), comment="입찰공고명")
    prtcpt_cnum = Column(String(6), comment="참가업체수")
    bidwinnr_nm = Column(String(100), comment="최종낙찰업체명")
    bidwinnr_bizno = Column(String(10), comment="최종낙찰업체사업자등록번호")
    bidwinnr_ceo_nm = Column(String(35), comment="최종낙찰업체대표자명")
    bidwinnr_adrs = Column(String(200), comment="최종낙찰업체주소")
    bidwinnr_tel_no = Column(String(25), comment="최종낙찰업체전화번호")
    sucsfbid_amt = Column(String(21), comment="최종낙찰금액")
    sucsfbid_rate = Column(String(18), comment="최종낙찰률")
    rl_openg_dt = Column(String(19), comment="실개찰일시")
    dminstt_cd = Column(String(7), comment="수요기관코드")
    dminstt_nm = Column(String(200), comment="수요기관명")
    rgst_dt = Column(String(19), comment="등록일시")
    fnl_sucsf_date = Column(String(10), comment="최종낙찰일자")
    fnl_sucsf_corp_ofcl = Column(String(35), comment="최종낙찰업체담당자")
