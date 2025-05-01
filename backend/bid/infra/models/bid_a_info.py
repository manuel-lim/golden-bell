from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String
from backend.database import Base


# 입찰가격산식A정보 조회
class BidAInfo(Base):
    __tablename__ = 'bid_a_info'

    bid_ntce_no = mapped_column(String, comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String, comment='입찰공고차수')
    sfty_mngcst = mapped_column(String, comment='안전관리비')
    sfty_chck_mngcst = mapped_column(String, comment='안전점검비')
    rtrfund_non = mapped_column(String, comment='환급비용 없음')
    mrfn_health_insrprm = mapped_column(String, comment='노인장기요양보험료')
    npn_insrprm = mapped_column(String, comment='국민연금보험료')
    odsn_lngtrmrcpr_insrprm = mapped_column(String, comment='산재장기요양보험료')
    qlty_mngcst = mapped_column(String, comment='품질관리비')
    qlty_mngcst_a_obj_yn = mapped_column(String, comment='품질관리비대상여부')
    prearng_prce_dcsn_mthd_nm = mapped_column(String, comment='예정가격결정방법명')
    ntce_ntice_dt = mapped_column(String, comment='공고일시')
    bid_prce_calcl_a_open_dt = mapped_column(String, comment='투찰가격 산정 공개일시')
