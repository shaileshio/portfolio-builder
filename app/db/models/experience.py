from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class Experience(Base, name="experiences"):
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

    company: Mapped[str] = mapped_column(
        String(length=200),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(length=200),
        nullable=False,
    )

    location: Mapped[str | None] = mapped_column(
        String(length=200),
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(length=100),
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
    )

    current: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="experiences",
    )
