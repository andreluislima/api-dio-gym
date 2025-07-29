
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat
from workout_api.categorias.categoria_schema import CategoriaSchemaIn
from workout_api.centro_treinamento.centro_treinamento_schema import CentroTreinamentoSchemaAtleta 

class AtletaSchema(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta',max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta',max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta')]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta')]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta')]
    genero: Annotated[str, Field(description='Gênero do Atleta', max_length=1)]
    
    categoria: Annotated[CategoriaSchemaIn, Field(description='Categoria do Atleta')]
    centro_treinamento: Annotated [CentroTreinamentoSchemaAtleta, Field(description='Centro de Treinamento do Atleta')]