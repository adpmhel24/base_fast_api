from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from starlette.middleware.cors import CORSMiddleware
from .api.api_v1.routers import api_router
from .core.config import settings

# from .api.api_v1.routers import api_router

from typing import Callable

from fastapi import Request, Response, HTTPException, APIRouter, FastAPI
from fastapi.routing import APIRoute
from .utils.logging import logger


class RouteErrorHandler(APIRoute):
    """Custom APIRoute that handles application errors and exceptions"""

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except Exception as ex:
                if isinstance(ex, HTTPException):
                    raise ex
                logger.exception("Uncaught error")
                # wrap error into pretty 500 exception
                raise HTTPException(status_code=500, detail=str(ex))

        return custom_route_handler


router = APIRouter(route_class=RouteErrorHandler)


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.include_router(router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"message": exc.errors()[0]["msg"]}),
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code, content=jsonable_encoder({"message": exc.detail})
    )


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def index():
    return {"title": "Welcome"}
