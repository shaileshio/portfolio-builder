from datetime import datetime
from typing import Annotated
from uuid import UUID

from sqlalchemy import DateTime, func, text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import mapped_column
from uuid6 import uuid7

IntIDPrimaryKey = Annotated[
    int,
    mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
    ),
]

UUID7PrimaryKey = Annotated[
    UUID,
    mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid7,
        server_default=text(text="uuidv7()"),
        nullable=False,
    ),
]

CreatedAt = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    ),
]

UpdatedAt = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    ),
]
