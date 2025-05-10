from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text, Integer
from backend.database import Base


"""
검색조건에 변경일시, 입찰공고번호를 입력하여 변경된 입찰공고번호, 입찰공고차수, 입찰분류번호, 재입찰번호, 변경항목명, 
변경전후값 등 공사 입찰공고변경 데이터 조회 
※ 변경이력 추출 대상 항목 PQ신청서접수일시, 물품분류제한여부, 제조여부, 입찰서개시일시, 입찰서마감일시, 개찰일시, 입찰자격등록일시, 
공동수급협정서마감일시, PQ신청서접수방법명, 참가가능지역, 면허제한코드, 설명회실시일시, 입찰참가제한여부, 공고서, 규격서, 공고규격화일, 
공동수급구성방식코드, 입찰계약방법코드, 공동수급구성방식,실적신청서접수일시, 공고명, 재입찰허용여부, 실적신청서접수방법코드,예가방법구분코드, 
집행관코드, 추첨복수예가개수, 배정예산금액,총예가개수, 추정가격, 내역입찰여부, 지사투찰허용여부
"""
class ConstructionHistory(Base):
    __tablename__ = 'bid_construction_history'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    bsns_div_nm = mapped_column(String(30), comment='업무구분명')
    chg_data_div_nm = mapped_column(String(30), comment='변경데이터구분명')
    chg_dt = mapped_column(String(19), comment='변경일시')
    bid_ntce_no = mapped_column(String(40), comment='입찰공고번호')
    bid_ntce_ord = mapped_column(String(3), comment='입찰공고차수')
    bid_clsfc_no = mapped_column(String(5), comment='입찰분류번호')
    rbid_no = mapped_column(String(11), comment='재입찰번호')
    chg_item_nm = mapped_column(String(200), comment='변경항목명')
    bfchg_val = mapped_column(Text, comment='변경전값')
    afchg_val = mapped_column(Text, comment='변경후값')
    lcns_lmt_cd_rgst_list = mapped_column(Text, comment='면허제한코드변경후목록')
