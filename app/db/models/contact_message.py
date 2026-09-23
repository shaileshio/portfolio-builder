from enum import StrEnum
from uuid import UUID

from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from .__types import CreatedAt, UUID7PrimaryKey


class ContactMessageStatus(StrEnum):
    NEW = "new"
    READ = "read"
    REPLIED = "replied"
    ARCHIVED = "archived"


class ContactMessage(Base, name="contact_messages"):
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

    name: Mapped[str] = mapped_column(
        String(length=150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(length=320),
        nullable=False,
    )

    subject: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[ContactMessageStatus] = mapped_column(
        Enum(
            enums=ContactMessageStatus,
            name="contact_message_status",
        ),
        default=ContactMessageStatus.NEW,
        nullable=False,
        index=True,
    )

    created_at: Mapped[CreatedAt]
