from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.types import UUID7PrimaryKey

if TYPE_CHECKING:
    from ._project import Project


class ProjectLink(Base, name="project_links"):
    id: Mapped[UUID7PrimaryKey]

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="projects.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
        index=True,
    )

    label: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(length=1000),
        nullable=False,
    )

    icon: Mapped[str | None] = mapped_column(
        String(length=100),
    )

    project: Mapped[Project] = relationship(
        back_populates="links",
    )
