from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import Settings, get_settings

settings: Settings = get_settings()


allow_origins: list[str] = settings.cors.allow_origins
allow_methods: list[str] = settings.cors.allow_methods
allow_headers: list[str] = settings.cors.allow_headers
allow_credentials: bool = settings.cors.allow_credentials


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=allow_origins,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
        allow_credentials=allow_credentials,
    )
