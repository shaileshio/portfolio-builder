from enum import StrEnum
from typing import TYPE_CHECKING, Any
from uuid import UUID

from sqlalchemy import JSON, Boolean, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class SectionType(StrEnum):
    HERO = "hero"
    ABOUT = "about"
    SKILLS = "skills"
    PROJECTS = "projects"
    EXPERIENCE = "experience"
    EDUCATION = "education"
    SERVICES = "services"
    TESTIMONIALS = "testimonials"
    BLOG = "blog"
    CONTACT = "contact"
    CUSTOM = "custom"


class PortfolioSection(Base, name="portfolio_sections"):
    id: Mapped[UUID7PrimaryKey]

    portfolio_id: Mapped[UUID] = mapped_column(
        ForeignKey(column="portfolios.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    type: Mapped[SectionType] = mapped_column(
        Enum(
            enums=SectionType,
            name="section_type",
        ),
        nullable=False,
    )

    title: Mapped[str | None] = mapped_column(
        String(length=255),
    )

    slug: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    config: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="sections",
    )
