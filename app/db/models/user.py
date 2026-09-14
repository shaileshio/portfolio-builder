from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from ._mixins import UUID7Mixin

if TYPE_CHECKING:
    from .profile import Profile


class User(UUID7Mixin, Base):
    __tablename__: str = "users"

    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    profile: Mapped[Profile | None] = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
    )
