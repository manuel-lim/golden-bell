from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Text

from backend.bid.infra.models.bid_etc import BidEtc
class BidEtcSearch(BidEtc):
    __tablename__ = 'bid_etc'
    pass
