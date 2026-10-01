from sqlalchemy import Index, String
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    status: Mapped[str] = mapped_column(String(50))

    __table_args__ = (
        Index("ix_documents_user_id", "user_id"),
        Index("ix_documents_status", "status"),
        Index("ix_documents_user_status", "user_id", "status"),
    )
