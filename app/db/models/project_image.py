from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .project import Project


class ProjectImage(Base, name="project_images"):
    id: Mapped[UUID7PrimaryKey]

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="projects.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    url: Mapped[str] = mapped_column(
        String(length=1000),
        nullable=False,
    )

    alt_text: Mapped[str | None] = mapped_column(
        String(length=255),
    )

    caption: Mapped[str | None] = mapped_column(
        String(length=500),
    )

    is_cover: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    project: Mapped[Project] = relationship(
        back_populates="images",
    )
