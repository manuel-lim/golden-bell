from sqlalchemy import DateTime, Index, Integer, String, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('unique_email', 'bid_manager_email_address', unique=True),
        Index('unique_phone_number', 'phone_number', unique=True),
        Index('unique_userid', 'user_id', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    name: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    password: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    role: Mapped[int] = mapped_column(TINYINT, server_default=text("'0'"))
    phone_number: Mapped[str] = mapped_column(String(30, 'utf8mb4_unicode_ci'))
    authenticated: Mapped[int] = mapped_column(TINYINT, server_default=text("'0'"), comment='인증 여부')
    status: Mapped[int] = mapped_column(TINYINT, server_default=text("'1'"), comment='회원상태')
    company_name: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='상호명')
    company_representative: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='대표자명')
    company_business_number: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='사업자번호')
    company_call_number: Mapped[str] = mapped_column(String(30, 'utf8mb4_unicode_ci'))
    company_zipcode: Mapped[str] = mapped_column(String(30, 'utf8mb4_unicode_ci'))
    company_address: Mapped[str] = mapped_column(String(200, 'utf8mb4_unicode_ci'), comment='회사주소')
    company_address_detail: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='업체 세부주소')
    company_business_type: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    company_email_address: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    company_special_type: Mapped[int] = mapped_column(TINYINT, server_default=text("'0'"))
    bid_manager_name: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='입찰담당자명')
    bid_manager_position: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='입찰담당자 직위')
    bid_manager_birthday: Mapped[str] = mapped_column(String(30, 'utf8mb4_unicode_ci'), comment='입찰담당자 생일')
    bid_manager_gender: Mapped[int] = mapped_column(TINYINT, server_default=text("'1'"))
    bid_manager_email_address: Mapped[str] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    bid_manage_is_agree_to_receive_important_info: Mapped[int] = mapped_column(TINYINT, server_default=text("'0'"), comment='주요정보수신동의 여부')
    bid_manager_bidding_experience: Mapped[int] = mapped_column(TINYINT, comment='입찰자 경력')
    joined_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    last_login_time: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
