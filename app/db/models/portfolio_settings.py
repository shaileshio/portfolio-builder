from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .__types import UUID7PrimaryKey

if TYPE_CHECKING:
    from .portfolio import Portfolio


class PortfolioSettings(Base, name="portfolio_settings"):
    id: Mapped[UUID7PrimaryKey]

    portfolio_id: Mapped[UUID] = mapped_column(
        ForeignKey(column="portfolios.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    show_resume: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    show_contact: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    show_blog: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    show_projects: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    show_experience: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    show_education: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    portfolio: Mapped[Portfolio] = relationship(
        back_populates="settings",
    )
