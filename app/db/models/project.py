from enum import StrEnum
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    Boolean,
    Enum,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import CreatedAt, UpdatedAt, UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio
    from .project_image import ProjectImage
    from .project_technology import ProjectTechnology


class ProjectStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Project(Base, name="projects"):
    id: Mapped[UUID7PrimaryKey]

    portfolio_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(length=200),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(length=220),
        nullable=False,
        index=True,
    )

    tagline: Mapped[str | None] = mapped_column(
        String(length=300),
    )

    short_description: Mapped[str] = mapped_column(
        String(length=500),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    problem: Mapped[str | None] = mapped_column(
        Text,
    )

    solution: Mapped[str | None] = mapped_column(
        Text,
    )

    architecture: Mapped[str | None] = mapped_column(
        Text,
    )

    challenges: Mapped[str | None] = mapped_column(
        Text,
    )

    results: Mapped[str | None] = mapped_column(
        Text,
    )

    lessons_learned: Mapped[str | None] = mapped_column(
        Text,
    )

    repository_url: Mapped[str | None] = mapped_column(
        String(1000),
    )

    demo_url: Mapped[str | None] = mapped_column(
        String(1000),
    )

    featured: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    status: Mapped[ProjectStatus] = mapped_column(
        Enum(
            enums=ProjectStatus,
            name="project_status",
        ),
        default=ProjectStatus.DRAFT,
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="projects",
    )

    technologies: Mapped[list[ProjectTechnology]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
    )

    images: Mapped[list[ProjectImage]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
    )
