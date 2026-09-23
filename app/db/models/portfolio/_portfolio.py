from enum import StrEnum
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.types import CreatedAt, UpdatedAt, UUID7PrimaryKey

if TYPE_CHECKING:
    from .. import (
        BlogPost,
        Certification,
        Education,
        Experience,
        PortfolioSEO,
        PortfolioSettings,
        Profile,
        Project,
        Service,
        Skill,
        SocialLink,
        Testimonial,
        User,
    )

_CASCADE_DELETE_ORPHAN = "all, delete-orphan"


class PortfolioStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Portfolio(Base, name="portfolios"):
    id: Mapped[UUID7PrimaryKey]

    owner_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="users.id",
            ondelete="SET NULL",
        ),
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(length=200),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(length=220),
        nullable=False,
        unique=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    status: Mapped[PortfolioStatus] = mapped_column(
        Enum(
            enums=PortfolioStatus,
            name="portfolio_status",
            native_enum=True,
        ),
        default=PortfolioStatus.DRAFT,
        nullable=False,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]

    owner: Mapped[User] = relationship(
        back_populates="portfolios",
    )

    profile: Mapped[Profile | None] = relationship(
        back_populates="portfolio",
        uselist=False,
        cascade=_CASCADE_DELETE_ORPHAN,
    )

    settings: Mapped[PortfolioSettings | None] = relationship(
        back_populates="portfolio",
        uselist=False,
        cascade=_CASCADE_DELETE_ORPHAN,
    )

    seo: Mapped[PortfolioSEO | None] = relationship(
        back_populates="portfolio",
        uselist=False,
        cascade=_CASCADE_DELETE_ORPHAN,
    )

    experiences: Mapped[list[Experience]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="Experience.sort_order",
    )

    educations: Mapped[list[Education]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="Education.sort_order",
    )

    certifications: Mapped[list[Certification]] = relationship(
        back_populates="certification",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="Certification.sort_order",
    )

    social_links: Mapped[list[SocialLink]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="SocialLink.sort_order",
    )

    skills: Mapped[list[Skill]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="Skill.sort_order",
    )

    projects: Mapped[list[Project]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="Project.sort_order",
    )

    services: Mapped[list[Service]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="Service.sort_order",
    )

    testimonials: Mapped[list[Testimonial]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
        order_by="Testimonial.sort_order",
    )

    blog_posts: Mapped[list[BlogPost]] = relationship(
        back_populates="portfolio",
        cascade=_CASCADE_DELETE_ORPHAN,
    )
