from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class Testimonial(Base, name="testimonials"):
    id: Mapped[UUID7PrimaryKey]

    portfolio_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="portfolios.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(length=200),
        nullable=False,
    )

    role: Mapped[str | None] = mapped_column(
        String(length=200),
    )

    company: Mapped[str | None] = mapped_column(
        String(length=200),
    )

    avatar_url: Mapped[str | None] = mapped_column(
        String(length=1000),
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    featured: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="testimonials",
    )
