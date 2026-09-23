from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .blog_post import BlogPost
    from .tag import Tag


class BlogPostTag(Base, name="blog_post_tags"):
    id: Mapped[UUID7PrimaryKey]

    post_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="blog_posts.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
        index=True,
    )

    tag_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="tags.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    post: Mapped[BlogPost] = relationship(
        back_populates="tags",
    )

    tag: Mapped[Tag] = relationship(
        back_populates="blog_post_tags",
    )
