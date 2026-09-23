from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .skill_category import SkillCategory


class Skill(Base, name="skills"):
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

    category_id: Mapped[UUID | None] = mapped_column(
        ForeignKey(
            column="skill_categories.id",
            ondelete="SET NULL",
        ),
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
    )

    proficiency: Mapped[int | None] = mapped_column(
        Integer,
    )

    years_experience: Mapped[int | None] = mapped_column(
        Integer,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    skill_category: Mapped[SkillCategory | None] = relationship(
        back_populates="skills",
    )
