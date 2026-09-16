from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from ._mixins import UUID7Mixin

if TYPE_CHECKING:
    from .skill import Skill


class SkillCategory(UUID7Mixin, Base):
    __tablename__: str = "skill_categories"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    skills: Mapped[list[Skill]] = relationship(
        back_populates="category",
    )
