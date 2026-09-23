from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class Education(Base, name="educations"):
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

    institution: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    degree: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    field_of_study: Mapped[str | None] = mapped_column(
        String(length=255),
    )

    start_date: Mapped[date | None] = mapped_column(
        Date,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    grade: Mapped[str | None] = mapped_column(
        String(length=100),
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="educations",
    )
