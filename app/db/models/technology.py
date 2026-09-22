from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from ._mixins import UUID7Mixin

if TYPE_CHECKING:
    from .profile_technologies import ProfileTechnology


class Technology(UUID7Mixin, Base):
    __tablename__: str = "technologies"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
        index=True,
    )

    icon: Mapped[str | None] = mapped_column(
        String(255),
    )

    profile_technologies: Mapped[list[ProfileTechnology]] = relationship(
        back_populates="technology",
        cascade="all, delete-orphan",
    )
