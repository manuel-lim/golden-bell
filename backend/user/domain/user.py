from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: int | None
    user_id: str
    name: str
    password: str
    role: int
    phone_number: str
    authenticated: int
    status: int
    company_name: str
    company_representative: str
    company_business_number: str
    company_call_number: str
    company_zipcode: str
    company_address: str
    company_address_detail: str
    company_business_type: str
    company_email_address: str
    company_special_type: int
    bid_manager_name: str
    bid_manager_position: str
    bid_manager_birthday: str
    bid_manager_gender: int
    bid_manager_email_address: str
    bid_manage_is_agree_to_receive_important_info: int
    bid_manager_bidding_experience: int
    joined_at: Optional[datetime] | None
    last_login_time: datetime | None
