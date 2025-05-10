from sqlalchemy.orm import DeclarativeBase, mapped_column, foreign
from sqlalchemy import String, Text, Integer, ForeignKey
from backend.bid.infra.models.etc import Etc

"""
나라장터검색조건에 의한 입찰공고 기타조회
"""
class G2BEtc(Etc):
    __tablename__ = 'bid_g2b_etc'

    id = mapped_column(Integer, ForeignKey('bid_etc.id'), primary_key=True, autoincrement=True)

