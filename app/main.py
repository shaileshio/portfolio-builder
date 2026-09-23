from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import Settings, get_settings

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

    app.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=allow_origins,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
        allow_credentials=allow_credentials,
    )

    return app


app: FastAPI = create_app()
