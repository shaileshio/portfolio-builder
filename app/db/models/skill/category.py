from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.types import UUID7PrimaryKey

if TYPE_CHECKING:
    from ._skill import Skill


class SkillCategory(Base, name="skill_categories"):
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
        String(length=100),
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    skills: Mapped[list[Skill]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )
