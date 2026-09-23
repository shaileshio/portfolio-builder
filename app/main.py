from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.core.config import Settings, get_settings
from app.core.exceptions.handlers import register_exception_handlers
from app.core.logging import configure_logging

configure_logging()

settings: Settings = get_settings()

title: str = settings.app.title
description: str = settings.app.description
api_prefix: str = settings.app.api_prefix
debug: bool = settings.app.debug


allow_origins: list[str] = settings.cors.allow_origins
allow_methods: list[str] = settings.cors.allow_methods
allow_headers: list[str] = settings.cors.allow_headers
allow_credentials: bool = settings.cors.allow_credentials


def create_app() -> FastAPI:
    app = FastAPI(
        title=title,
        description=description,
        api_prefix=api_prefix,
        debug=debug,
    )

    register_exception_handlers(app)

    app.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=allow_origins,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
        allow_credentials=allow_credentials,
    )

    return app


app: FastAPI = create_app()


@app.get(path="/", include_in_schema=False)
def root(request: Request) -> RedirectResponse:
    return RedirectResponse(url="/docs", status_code=307)
