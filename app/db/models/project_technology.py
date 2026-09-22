from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .project import Project
    from .technology import Technology


class ProjectTechnology(Base, name="project_technologies"):
    id: Mapped[UUID7PrimaryKey]

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="projects.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    technology_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="technologies.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    project: Mapped[Project] = relationship(
        back_populates="technologies",
    )

    technology: Mapped[Technology] = relationship(
        back_populates="project_technologies",
    )
