from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ARRAY, Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.types import UUID7PrimaryKey

if TYPE_CHECKING:
    from ._portfolio import Portfolio


class PortfolioSEO(Base, name="portfolio_seo"):
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

    title: Mapped[str | None] = mapped_column(
        String(length=255),
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    keywords: Mapped[list[str]] = mapped_column(
        ARRAY(item_type=String),
        nullable=False,
        default=list,
    )

    og_image_url: Mapped[str | None] = mapped_column(
        String(length=1000),
    )

    canonical_url: Mapped[str | None] = mapped_column(
        String(length=1000),
    )

    no_index: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="seo",
    )
