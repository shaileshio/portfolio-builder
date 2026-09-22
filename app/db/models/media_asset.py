from enum import StrEnum
from uuid import UUID

from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from .__types import UUID7PrimaryKey


class MediaType(StrEnum):
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"
    OTHER = "other"


class MediaAsset(Base, name="media_assets"):
    id: Mapped[UUID7PrimaryKey]

    portfolio_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="portfolios.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    type: Mapped[MediaType] = mapped_column(
        Enum(
            enums=MediaType,
            name="media_type",
        ),
        nullable=False,
    )

    filename: Mapped[str] = mapped_column(
        String(length=500),
        nullable=False,
    )

    storage_key: Mapped[str] = mapped_column(
        String(length=1000),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(length=2000),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
    )

    size_bytes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    width: Mapped[int | None] = mapped_column(
        Integer,
    )

    height: Mapped[int | None] = mapped_column(
        Integer,
    )

    alt_text: Mapped[str | None] = mapped_column(
        String(length=500),
    )
