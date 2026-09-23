from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.types import UUID7PrimaryKey


class Tag(Base, name="tags"):
    id: Mapped[UUID7PrimaryKey]

    name: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
        unique=True,
    )

    slug: Mapped[str] = mapped_column(
        String(length=120),
        nullable=False,
        unique=True,
        index=True,
    )
