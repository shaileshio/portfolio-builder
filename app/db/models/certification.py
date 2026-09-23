from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class Certification(Base, name="certifications"):
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

    name: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    issuer: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    credential_id: Mapped[str | None] = mapped_column(
        String(length=255),
    )

    credential_url: Mapped[str | None] = mapped_column(
        String(length=1000),
    )

    issued_at: Mapped[date | None] = mapped_column(
        Date,
    )

    expires_at: Mapped[date | None] = mapped_column(
        Date,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="certifications",
    )
