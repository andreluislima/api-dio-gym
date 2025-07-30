
from uuid import UUID, uuid4
from fastapi import APIRouter, Body, status
from sqlalchemy import select
from workout_api.centro_treinamento.centro_treinamento_schema import CentroTreinamentoSchemaOut
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.centro_treinamento.centro_treinamento_schema import CentroTreinamentoSchemaIn
from workout_api.centro_treinamento.centro_treinamento_model import CentroTreinamentoModel
from fastapi import HTTPException

router = APIRouter()

# INSERT
@router.post(
    path='/',
    summary='Criar novo CT',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoSchemaOut
)
async def Post(
    db_session:DatabaseDependency, 
    CentroTreinamentoSchemaIn: CentroTreinamentoSchemaIn = Body()
)-> CentroTreinamentoSchemaOut: # type: ignore
    
    centroTreinamentoOut = CentroTreinamentoSchemaOut(id=uuid4(), ** CentroTreinamentoSchemaIn.model_dump()) 
    centroTreinamentoModel = CentroTreinamentoModel(**centroTreinamentoOut.model_dump())
    
    db_session.add(centroTreinamentoModel)
    await db_session.commit()
    await db_session.refresh(centroTreinamentoModel)
    
    return centroTreinamentoOut


# GET ALL
@router.get(
    path='/',
    summary='Consultar todos os CTs',
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoSchemaOut]
)
async def query(db_session:DatabaseDependency)-> list[CentroTreinamentoSchemaOut]: # type: ignore
    result = await db_session.execute(select(CentroTreinamentoModel))
    centroTreinamentoModel = result.scalars().all()
    centroTreinamentoOut = [CentroTreinamentoSchemaOut.model_validate(categoria) for categoria in centroTreinamentoModel]
    
    return centroTreinamentoOut

# GET BY ID
@router.get(
    path='/{id}',
    summary='Consultar CT pelo ID',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoSchemaOut
    
)
async def query(id: UUID, db_session:DatabaseDependency) -> CentroTreinamentoSchemaOut: # type: ignore

    centro_treinamento: CentroTreinamentoSchemaOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id = id))).scalars().first() #type: ignore
    
    if not centro_treinamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f'CT não encontrado para o id {id}'
        )
    return centro_treinamento