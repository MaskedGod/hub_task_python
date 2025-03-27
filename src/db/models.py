from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .database import Base


class URLModel(Base):
    __tablename__ = "urls"

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    original_url: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    short_url: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"original_url={self.original_url}, short_url={self.short_url}"
