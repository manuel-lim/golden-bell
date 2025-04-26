from enum import StrEnum

class BidType(StrEnum):
    CONSTRUCTION = 'construction'
    IMPORTED = 'imported'
    OUTSOURCING = 'outsourcing'
    PRODUCT = 'product'