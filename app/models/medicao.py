from datetime import datetime

from sqlalchemy import ForeignKey, Float, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Medicao(Base):
    __tablename__ = "medicoes"

    id: Mapped[int] = mapped_column(primary_key=True)

    host_id: Mapped[int] = mapped_column(
        ForeignKey("hosts.id")
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    latencia_ms: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    perda_pacotes: Mapped[float] = mapped_column(
        Float
    )

    status: Mapped[str] = mapped_column(
        String(20)
    )