from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class Profile(Base, name="profiles"):
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

    first_name: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
    )

    last_name: Mapped[str | None] = mapped_column(
        String(length=100),
    )

    headline: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    bio: Mapped[str | None] = mapped_column(
        Text,
    )

    email: Mapped[str | None] = mapped_column(
        String(length=320),
    )

    phone: Mapped[str | None] = mapped_column(
        String(length=50),
    )

    location: Mapped[str | None] = mapped_column(
        String(length=200),
    )

    avatar_url: Mapped[str | None] = mapped_column(
        String(length=1000),
    )

    resume_url: Mapped[str | None] = mapped_column(
        String(length=1000),
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="profile",
    )
