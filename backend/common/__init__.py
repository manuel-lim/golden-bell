from enum import StrEnum

class BidType(StrEnum):
    CONSTRUCTION = 'construction'
    SERVICE = 'service'
    FOREIGN_PROCUREMENT = 'foreign_procurement'
    PRODUCT = 'product'