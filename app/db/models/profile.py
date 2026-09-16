import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from ._mixins import TimestampMixin, UUID7Mixin

if TYPE_CHECKING:
    from .skill import Skill
    from .social_link import SocialLink
    from .user import User


class Profile(UUID7Mixin, TimestampMixin, Base):
    __tablename__: str = "profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    headline: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    bio: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
    )

    location: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
    )

    avatar_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    user: Mapped[User] = relationship(
        "User",
        back_populates="profile",
    )

    social_links: Mapped[list[SocialLink]] = relationship(
        "SocialLink",
        back_populates="profile",
        cascade="all, delete-orphan",
    )

    skills: Mapped[list[Skill]] = relationship(
        back_populates="profile",
        cascade="all, delete-orphan",
    )
