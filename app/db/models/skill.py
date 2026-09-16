from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from ._mixins import UUID7Mixin

if TYPE_CHECKING:
    from .profile import Profile
    from .skill_category import SkillCategory


class Skill(UUID7Mixin, Base):
    __tablename__: str = "skills"

    profile_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(
            "profiles.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(
            "skill_categories.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    proficiency: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    profile: Mapped[Profile] = relationship(
        back_populates="skills",
    )

    category: Mapped[SkillCategory] = relationship(
        back_populates="skills",
    )
