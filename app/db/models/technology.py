from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .project_technology import ProjectTechnology


class Technology(Base, name="technologies"):
    id: Mapped[UUID7PrimaryKey]

    name: Mapped[str] = mapped_column(
        String(length=100),
        unique=True,
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(length=120),
        unique=True,
        nullable=False,
        index=True,
    )

    icon: Mapped[str | None] = mapped_column(
        String(length=255),
    )

    website_url: Mapped[str | None] = mapped_column(
        String(length=1000),
    )

    project_technologies: Mapped[list[ProjectTechnology]] = relationship(
        back_populates="technology",
        cascade="all, delete-orphan",
    )
