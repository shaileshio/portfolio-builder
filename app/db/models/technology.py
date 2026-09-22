from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from .__types import UUID7PrimaryKey


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
