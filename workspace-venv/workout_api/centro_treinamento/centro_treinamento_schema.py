from workout_api.contrib.schemas import BaseSchema
from pydantic import UUID4, Field
from typing import Annotated

class CentroTreinamentoSchemaIn(BaseSchema):
    nome:Annotated[str, Field(description='CT King', max_length=30)]
    endereco:Annotated[str, Field(description='Endereço do CT', max_length=60)]
    propietario:Annotated[str, Field(description='Propietario do CT', max_length=30)]
    

class CentroTreinamentoSchemaAtleta(BaseSchema):
    nome:Annotated[str, Field(description='Nome do Centro de Treinamento', max_length=30)]

class CentroTreinamentoSchemaOut(CentroTreinamentoSchemaIn):
    id: Annotated[UUID4, Field(description='Identificador de Centro de Treinamento')]
    
    class Config: # type: ignore
        from_attributes = True