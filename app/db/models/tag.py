from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .blog_post import BlogPostTag


class Tag(Base, name="tags"):
    id: Mapped[UUID7PrimaryKey]

    name: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False,
        unique=True,
    )

    slug: Mapped[str] = mapped_column(
        String(length=120),
        nullable=False,
        unique=True,
        index=True,
    )

    blog_post_tags: Mapped[list[BlogPostTag]] = relationship(
        back_populates="tag",
    )
