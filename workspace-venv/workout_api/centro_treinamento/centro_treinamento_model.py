from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

if TYPE_CHECKING:
    from workout_api.atleta.atleta_model import AtletaModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centro_treinamento"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(30), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    propietario: Mapped[str] = mapped_column(String(30), nullable=False)
    
    atletas: Mapped[list["AtletaModel"]] = relationship("AtletaModel", back_populates="centro_treinamento")
