from uuid import UUID, uuid4
from fastapi import APIRouter, Body, status
from sqlalchemy import select
from workout_api.categoria.categoria_schema import CategoriaSchemaIn, CategoriaSchemaOut
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.categoria.categoria_model import CategoriaModel
from fastapi import HTTPException

router = APIRouter()

# INSERT
@router.post(
    path='/',
    summary='Criar nova Categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaSchemaOut
)
async def Post(
    db_session: DatabaseDependency,
    CategoriaSchemaIn: CategoriaSchemaIn = Body()
) -> CategoriaSchemaOut: # type: ignore
    
    categoriaOut = CategoriaSchemaOut(id=uuid4(), ** CategoriaSchemaIn.model_dump())
    categoriaModel = CategoriaModel(**categoriaOut.model_dump())
    
    db_session.add(categoriaModel)
    await db_session.commit()
    await db_session.refresh(categoriaModel)
    
    return categoriaOut


# GET ALL
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

# GET BY ID
@router.get(
    path='/{id}',
    summary='Consutar Categoria pelo Id',
    status_code=status.HTTP_404_NOT_FOUND,
    response_model=CategoriaSchemaOut
)
async def query(id: UUID, db_session:DatabaseDependency) -> CategoriaSchemaOut: #type: ignore
    
    categoria: CategoriaSchemaOut = (await db_session.execute(select(CategoriaModel).filter_by(id = id))).scalars().first() #type: ignore
     
    if not categoria: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada para o id {id}'
        )   
        
    return categoria
    