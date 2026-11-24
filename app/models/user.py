from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.ticket import Ticket

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
    String(255),
    nullable=False,
)
    is_admin: Mapped[bool] = mapped_column(
    Boolean,
    default=False,
    nullable=False,
)
    tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="user"
    )