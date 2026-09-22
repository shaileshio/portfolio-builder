import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from .profile import Profile
    from .technology import Technology


class ProfileTechnology(Base):
    __tablename__: str = "profile_technologies"

    profile_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("profiles.id", ondelete="CASCADE"),
        primary_key=True,
    )

    technology_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("technologies.id", ondelete="CASCADE"),
        primary_key=True,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    profile: Mapped[Profile] = relationship(
        back_populates="profile_technologies",
    )

    technology: Mapped[Technology] = relationship(
        back_populates="profile_technologies",
    )
