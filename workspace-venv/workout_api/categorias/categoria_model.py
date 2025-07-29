from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

if TYPE_CHECKING:
    from workout_api.atleta.atleta_model import AtletaModel

class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
    atletas: Mapped[list["AtletaModel"]] = relationship(back_populates="categoria")
