from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.types import CreatedAt, UpdatedAt, UUID7PrimaryKey

if TYPE_CHECKING:
    from ..portfolio import Portfolio
    from .blog_post_tag import BlogPostTag


class BlogPostStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class BlogPost(Base, name="blog_posts"):
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

    title: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(length=280),
        nullable=False,
        index=True,
    )

    excerpt: Mapped[str | None] = mapped_column(
        String(length=500),
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[BlogPostStatus] = mapped_column(
        Enum(
            enums=BlogPostStatus,
            name="blog_post_status",
        ),
        default=BlogPostStatus.DRAFT,
        nullable=False,
    )

    published_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="blog_posts",
    )

    tags: Mapped[list[BlogPostTag]] = relationship(
        back_populates="blog_post",
        cascade="all, delete-orphan",
    )
