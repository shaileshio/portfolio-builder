import fastapi_swagger_ui_theme
from fastapi import FastAPI

from app.core.config import Settings, get_settings

settings: Settings = get_settings()

title: str = settings.app.title


def setup_swagger_ui(app: FastAPI) -> None:
    fastapi_swagger_ui_theme.setup_swagger_ui_theme(
        app=app,
        docs_path="/",
        title=f"{title} - API Docs",
    )
