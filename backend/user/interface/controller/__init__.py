from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional

class UserBody(BaseModel):
    user_id: str = Field(min_length=3, max_length=100)
    name: str = Field(min_length=3, max_length=100)
    password: str = Field(default=None, min_length=3, max_length=100)
    role: int
    phone_number: Optional[str] = Field(min_length=10, max_length=11)
    authenticated: Optional[int] = None
    status: Optional[int] = None
    company_name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    company_representative: Optional[str] = Field(default=None, min_length=3, max_length=100)
    company_business_number: Optional[str] = Field(default=None, min_length=3, max_length=100)
    company_call_number: Optional[str] = Field(default=None, min_length=3, max_length=100)
    company_zipcode: Optional[str] = Field(default=None, min_length=3, max_length=10)
    company_address: Optional[str] = Field(default=None, min_length=3, max_length=100)
    company_address_detail: Optional[str] = Field(default=None, min_length=3, max_length=100)
    company_business_type: Optional[str] = None
    company_email_address: Optional[str] = None
    company_special_type: Optional[int] = None
    bid_manager_name: Optional[str] = None
    bid_manager_position: Optional[str] = None
    bid_manager_birthday: Optional[str] = None
    bid_manager_gender: Optional[int] = None
    bid_manager_email_address: Optional[str] = None
    bid_manage_is_agree_to_receive_important_info: Optional[int] = None
    bid_manager_bidding_experience: Optional[int] = None


class CreateUserBody(UserBody):
    pass


class UpdateUserBody(UserBody):
    def __iter__(self):
        yield 'user_id', self.user_id
        yield 'name', self.name
        yield 'password', self.password
        yield 'role', self.role
        yield 'phone_number', self.phone_number
        yield 'authenticated', self.authenticated
        yield 'status', self.status
        yield 'company_name', self.company_name
        yield 'company_representative', self.company_representative
        yield 'company_business_number', self.company_business_number
        yield 'company_call_number', self.company_call_number
        yield 'company_zipcode', self.company_zipcode
        yield 'company_address', self.company_address_detail
        yield 'company_address_detail', self.company_address_detail
        yield 'company_business_type', self.company_business_type
        yield 'company_email_address', self.company_email_address
        yield 'company_special_type', self.company_special_type
        yield 'bid_manager_name', self.bid_manager_name
        yield 'bid_manager_position', self.bid_manager_position
        yield 'bid_manager_birthday', self.bid_manager_birthday
        yield 'bid_manager_gender', self.bid_manager_gender
        yield 'bid_manager_email_address', self.bid_manager_email_address
        yield 'bid_manage_is_agree_to_receive_important_info', self.bid_manage_is_agree_to_receive_important_info
        yield 'bid_manager_bidding_experience', self.bid_manager_bidding_experience


class UserResponse(UserBody):
    id: int
    joined_at: datetime
    last_login_time: datetime


class GetUsersResponse(BaseModel):
    total_count: int
    page: int
    users: list[UserResponse]


class PostUserResponse(BaseModel):
    code: int
    message: str
    data: Optional[UserResponse] = None


class PutUserResponse(BaseModel):
    code: int
    message: str
    data: Optional[UserResponse] = None

