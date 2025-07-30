from uuid import UUID, uuid4
from fastapi import APIRouter, Body, status
from sqlalchemy import select
from workout_api.categoria.categoria_schema import CategoriaSchemaIn, CategoriaSchemaOut
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.categoria.categoria_model import CategoriaModel
from fastapi import HTTPException

router = APIRouter()

@router.get(
    path='/',
    summary='Consultar todas as categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaSchemaOut]
)
async def query(db_session: DatabaseDependency) -> list[CategoriaSchemaOut]:  # type: ignore
    
    # categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all() # type: ignore
    
    result = await db_session.execute(select(CategoriaModel))
    categorias_model = result.scalars().all()
    categorias_out = [CategoriaSchemaOut.model_validate(categoria) for categoria in categorias_model]
    
    return categorias_out   