from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import mapped_column
from backend.database import Base

class BidNotice(Base):
    __tablename__ = 'bid_notice'
    id = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    construction_id = mapped_column(BigInteger, ForeignKey('bid_construction.id'))
    service_id = mapped_column(BigInteger, ForeignKey('bid_service.id'))
    foreign_procurement_id = mapped_column(BigInteger, ForeignKey('bid_foreign_procurement.id'))
    product_id = mapped_column(BigInteger, ForeignKey('bid_product.id'))
