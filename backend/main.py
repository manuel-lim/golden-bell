from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from backend.containers import Container
from backend.user.interface.controller.user_controller import  router as user_router

app = FastAPI()

app.include_router(user_router)
app.container = Container()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	return JSONResponse(status_code=400, content=exc.errors())