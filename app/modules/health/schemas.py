from typing import Literal

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: Literal["ok"]


class HealthReadyResponse(BaseModel):
    status: Literal["ok"]
    database: Literal["connected"]


class HealthReadyErrorResponse(BaseModel):
    status: Literal["error"]
    database: Literal["disconnected"]
