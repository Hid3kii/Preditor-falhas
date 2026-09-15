from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Host(Base):
    __tablename__ = "hosts"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    endereco_ip: Mapped[str] = mapped_column(String(45), unique=True)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)