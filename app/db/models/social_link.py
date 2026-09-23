from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class SocialLink(Base, name="social_links"):
    id: Mapped[UUID7PrimaryKey]

    portfolio_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="portfolios.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
        index=True,
    )

    platform: Mapped[str] = mapped_column(
        String(length=50),
        nullable=False,
    )

    label: Mapped[str | None] = mapped_column(
        String(length=100),
    )

    url: Mapped[str] = mapped_column(
        String(length=1000),
        nullable=False,
    )

    icon: Mapped[str | None] = mapped_column(
        String(length=100),
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="social_links",
    )
