from enum import StrEnum
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import CreatedAt, UpdatedAt, UUID7PrimaryKey

if TYPE_CHECKING:
    from . import PortfolioSEO, PortfolioSettings, PortfolioTheme, Profile, User


class PortfolioStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


_CASCADE_DELETE_ORPHAN = "all, delete-orphan"


class Portfolio(Base, name="portfolios"):
    id: Mapped[UUID7PrimaryKey]

    owner_id: Mapped[UUID] = mapped_column(
        ForeignKey(column="users.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(length=200),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(length=220),
        unique=True,
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    status: Mapped[PortfolioStatus] = mapped_column(
        Enum(
            enums=PortfolioStatus,
            name="portfolio_status",
            native_enum=True,
        ),
        default=PortfolioStatus.DRAFT,
        nullable=False,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]

    owner: Mapped[User] = relationship(
        back_populates="portfolios",
    )

    profile: Mapped[Profile | None] = relationship(
        back_populates="portfolio",
        uselist=False,
        cascade=_CASCADE_DELETE_ORPHAN,
    )

    settings: Mapped[PortfolioSettings | None] = relationship(
        back_populates="portfolio",
        uselist=False,
        cascade=_CASCADE_DELETE_ORPHAN,
    )

    theme: Mapped[PortfolioTheme | None] = relationship(
        back_populates="portfolio",
        uselist=False,
        cascade=_CASCADE_DELETE_ORPHAN,
    )

    seo: Mapped[PortfolioSEO | None] = relationship(
        back_populates="portfolio",
        uselist=False,
        cascade="all, delete-orphan",
    )
