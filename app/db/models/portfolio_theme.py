from typing import TYPE_CHECKING, Any
from uuid import UUID

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class PortfolioTheme(Base, name="portfolio_themes"):
    id: Mapped[UUID7PrimaryKey]

    portfolio_id: Mapped[UUID] = mapped_column(
        ForeignKey(column="portfolios.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    template: Mapped[str] = mapped_column(
        String(length=100),
        default="minimal",
        nullable=False,
    )

    primary_color: Mapped[str] = mapped_column(
        String(length=20),
        default="#111827",
        nullable=False,
    )

    accent_color: Mapped[str] = mapped_column(
        String(length=20),
        default="#2563eb",
        nullable=False,
    )

    font_heading: Mapped[str] = mapped_column(
        String(length=100),
        default="Inter",
        nullable=False,
    )

    font_body: Mapped[str] = mapped_column(
        String(length=100),
        default="Inter",
        nullable=False,
    )

    config: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="theme",
    )
