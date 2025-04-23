from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import Provide, inject
from fastapi.security import OAuth2PasswordRequestForm

from backend.containers import Container
from backend.user.application.user_service import UserService

import logging
from backend.utils.db_utils import row_to_dict
from backend.utils import props

from backend.user.interface.controller import *
from backend.common.auth import CurrentUser, get_current_user

router = APIRouter(prefix="/user")
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


@router.get('/list', response_model=GetUsersResponse)
@inject
def get_users(page: int = 1,
              per_page: int = 10,
              user_service: UserService = Depends(Provide[Container.user_service])) -> GetUsersResponse:
    total_count, users_ = user_service.get_users(page, per_page)
    users = [UserResponse(**row_to_dict(user)) for user in users_]
    return GetUsersResponse(total_count=total_count, page=page, users=users)


@router.post('/join', response_model=PostUserResponse)
@inject
def create_user(user_body: CreateUserBody, user_service: UserService = Depends(Provide[Container.user_service])) -> PostUserResponse:
    response = None
    try:
        user = user_service.create_user(user_body)
        response = PostUserResponse(code=200, message='success', data=UserResponse(**props(user)))

    except HTTPException as e:
        if e.status_code == 400:
            response = PostUserResponse(code=400, message=e.detail, data=None)
        else:
            response = PostUserResponse(code=500, message=e.detail, data=None)

    except Exception as e:
        response = PostUserResponse(code=500, message=str(e), data=None)

    finally:
        return response


@router.put('/update', response_model=PostUserResponse)
@inject
def update_user(
        current_user: Annotated[CurrentUser, Depends(get_current_user)],
        body: UpdateUserBody,
        user_service: UserService = Depends(Provide[Container.user_service])) -> PutUserResponse:

    response = None
    try:
        result = user_service.update_user(current_user.user_id, body)
        response = PutUserResponse(code=200, message='success', data=UserResponse(**props(result)))

    except HTTPException as e:
        if e.status_code == 422:
            response = PutUserResponse(code=422, message=e.detail, data=None)
        else:
            response = PutUserResponse(code=500, message=e.detail, data=None)

    finally:
        return response


@router.post('/login')
@inject
def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        user_service: UserService = Depends(Provide[Container.user_service])
    ):
    access_token = user_service.login(form_data.username, form_data.password)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.delete('/delete')
@inject
def delete_user(
        current_user: Annotated[CurrentUser, Depends(get_current_user)],
        user_service: UserService = Depends(Provide[Container.user_service])
):
    result = user_service.delete_user(current_user.user_id)
    return {'code': 200, 'message': 'success'} if result else {'code': 404, 'message': 'user not found'}
