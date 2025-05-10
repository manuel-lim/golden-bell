from sqlalchemy.orm import mapped_column
from sqlalchemy import String, BigInteger, DateTime, text
from backend.database import Base


class OpenServicePrice(Base):
    __tablename__ = 'win_bid_open_service_price'
    __table_args__ = {'comment': '개찰결과 용역 예비가격상세 목록 조회'}

    id = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    bid_ntce_no = mapped_column(String(11), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(3), comment='재입찰번호')
    bid_ntce_nm = mapped_column(String(100), comment='입찰공고명')
    plnprc = mapped_column(String(21), comment='예정가격')
    bssamt = mapped_column(String(21), comment='기초금액')
    tot_rsrvtn_prce_num = mapped_column(String(2), comment='총예가건수')
    compno_rsrvtn_prce_sno = mapped_column(String(6), comment='복수예가순번')
    bsis_plnprc = mapped_column(String(21), comment='기초예정가격')
    drwt_yn = mapped_column(String(1), comment='추첨여부')
    drwt_num = mapped_column(String(22), comment='추첨횟수')
    bidwinr_slctn_apl_bss_cntnts = mapped_column(String(200), comment='최종낙찰자선정적용기준내용')
    rl_openg_dt = mapped_column(String(19), comment='실개찰일시')
    bssamt_bss_up_num = mapped_column(String(2), comment='기초금액기준상위건수')
    compno_rsrvtn_prce_mkng_dt = mapped_column(String(19), comment='복수예비가격작성일시')
    inpt_dt = mapped_column(String(19), comment='입력일시')
    prearng_prce_purcnstcst = mapped_column(String(22), comment='예정가격순공사비')
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))