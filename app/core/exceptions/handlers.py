from collections.abc import Callable
from logging import Logger, getLogger
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from .errors import AppError, HttpError

logger: Logger = getLogger(__name__)


def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    logger.debug("Application error: %s", exc.detail)

    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"detail": exc.detail},
    )


def http_error_handler(request: Request, exc: HttpError) -> JSONResponse:
    logger.debug("Application error: %s", exc.detail)

    return JSONResponse(
        status_code=exc.status,
        content={"code": exc.code, "detail": exc.detail},
    )


def unhandled_error_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception(
        msg="Unhandled exception: %s %s",
        extra={
            "path": request.url.path,
            "method": request.method,
        },
    )

    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred"},
    )


type ErrorHandler = Callable[[Request, Any], JSONResponse]


ERROR_HANDLERS: tuple[tuple[type[Exception], ErrorHandler], ...] = (
    (AppError, app_error_handler),
    (HttpError, http_error_handler),
    (Exception, unhandled_error_handler),
)


def setup_error_handlers(app: FastAPI) -> None:
    for exc, handler in ERROR_HANDLERS:
        app.add_exception_handler(exc, handler)
