from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import CreatedAt, UpdatedAt, UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class User(Base, name="users"):
    id: Mapped[UUID7PrimaryKey]

    email: Mapped[str] = mapped_column(
        __name_pos=String(length=320),
        nullable=False,
        unique=True,
        index=True,
    )

    password_hash: Mapped[str | None] = mapped_column(
        __name_pos=String(length=255),
    )

    is_active: Mapped[bool] = mapped_column(
        __name_pos=Boolean,
        default=True,
        nullable=False,
    )

    is_verified: Mapped[bool] = mapped_column(
        __name_pos=Boolean,
        default=False,
        nullable=False,
    )

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]

    portfolios: Mapped[list[Portfolio]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
