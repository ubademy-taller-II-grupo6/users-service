from fastapi import status, Request, FastAPI
from starlette.responses import JSONResponse

from app.utils import create_message_response
from app.exceptions import (
    InvalidEmailException,
    InvalidNameException,
    InvalidLastnameException,
    UserAlreadyExistException,
    InvalidUserIdException
)


async def invalid_email_exception_handler(request: Request, exc: InvalidEmailException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=create_message_response(exc.message))


async def invalid_name_exception_handler(request: Request, exc: InvalidNameException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=create_message_response(exc.message))


async def invalid_lastname_exception_handler(request: Request, exc: InvalidLastnameException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=create_message_response(exc.message))


async def user_already_exist_exception_handler(request: Request, exc: UserAlreadyExistException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=create_message_response(exc.message))


async def user_invalid_user_id_exception_handler(request: Request, exc: InvalidUserIdException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=create_message_response(exc.message))


def add_user_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidEmailException, invalid_email_exception_handler)
    app.add_exception_handler(InvalidNameException, invalid_name_exception_handler)
    app.add_exception_handler(InvalidLastnameException, invalid_lastname_exception_handler)
    app.add_exception_handler(UserAlreadyExistException, user_already_exist_exception_handler)
    app.add_exception_handler(InvalidUserIdException, user_invalid_user_id_exception_handler)