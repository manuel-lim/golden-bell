from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.testclient import TestClient

from backend.main import app
from backend.user.domain.user import User as UserVo
from backend.user.interface.controller import UpdateUserBody
from backend.user.interface.controller.user_controller import CreateUserBody
from backend import main
from backend.utils.crypto import Crypto
from backend.utils import props
import datetime
import ujson as json

from backend.user.application.user_service import UserService

client = TestClient(main.app)

from unittest.mock import MagicMock
def mock_get_db():
    mock_db = MagicMock()
    # Setup mock db
    return mock_db

def test_get_users():
    response = client.get("/user/list")
    assert response.status_code == 200

def test_join_user():
    crypto = Crypto()
    now = datetime.datetime.now()
    now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
    body = CreateUserBody(
        user_id='aaa33',
        name= '임재호',
        password = crypto.encrypt('임재호'),
        role = 1,
        phone_number = '01097151505',
        authenticated = 0,
        status = 1,
        company_name = 'SKT',
        company_representative = 'James',
        company_business_number = '123456789',
        company_call_number = '123456789',
        company_zipcode = '987654321',
        company_address = '서울특별시 중구 을지로65',
        company_address_detail = '33층',
        company_business_type = '1',
        company_email_address = 'a@skt.com',
        company_special_type = 1,
        bid_manager_name = 'abc',
        bid_manager_position = '이사',
        bid_manager_birthday = '2024-05-01',
        bid_manager_gender = 1,
        bid_manager_email_address = 'abc@skt.com',
        bid_manage_is_agree_to_receive_important_info = 1,
        bid_manager_bidding_experience = 1,
    )

    response = client.post("/user/join", json=body.model_dump_json(), headers={"Content-Type": "application/json"})
    assert response.status_code == 200

    assert response.json().get('status') == 1
    assert response.json().get('name') == '임재호'

class MockUserService:
    def get_current_user(self):
        return {"username": "aaa333", "password": "임재호"}

def override_user_service():
    return MockUserService()

app.dependency_overrides[UserService.get_user_service] = override_user_service

def test_update_user():
    crypto = Crypto()
    now = datetime.datetime.now()
    now = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
    body = UpdateUserBody(
        user_id='aaa333',
        name= '임재호2',
        password = crypto.encrypt('임재호2'),
        phone_number = '01097151506',
        company_representative='유영상',
        bid_manager_name = '강남역',
        role=1
    )


    f = OAuth2PasswordRequestForm(username='aaa333', password='임재호')
    # k = service.login(f.username, f.password)
    # resp = client.post('/user/login', json=json.dumps({'username': f.username, 'password': f.password}), headers={"Content-Type": "application/json"})
    # access_token = k.get('access_token')

    # response = client.put("/user/update", json=body.model_dump_json(exclude_none=True), headers={"Content-Type": "application/json", 'Authorization': 'Bearer ' + access_token})
    # assert response.status_code == 200
    # assert response.json().get('name') == '임재호2'
    # assert response.json().get('company_representative') == '유영상'
    # assert response.json().get('bid_manager_name') == '강남역'