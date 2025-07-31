from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4
from fastapi import APIRouter, Body, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from workout_api.atleta.atleta_model import AtletaModel
from workout_api.atleta.atleta_schema import AtletaSchemaIn, AtletaSchemaOut, AtletaSchemaUpdate, AtletaSchemaListOut
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.categoria.categoria_model import CategoriaModel
from workout_api.categoria.categoria_schema import CategoriaSchemaOut, CategoriaSchemaIn
from workout_api.centro_treinamento.centro_treinamento_model import CentroTreinamentoModel
from workout_api.centro_treinamento.centro_treinamento_schema import CentroTreinamentoSchemaOut, CentroTreinamentoSchemaAtleta

router = APIRouter()

# INSERT
@router.post(
    path='/',
    summary='Criar um novo registro de Atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaSchemaOut
)
async def post(
    db_session:DatabaseDependency,
    atleta_in: AtletaSchemaIn = Body()
)-> AtletaSchemaOut: # type:ignore
    
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
    
    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome = categoria_nome))).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail=f'A categoria {categoria_nome} não foi encontrada'
        )
        
    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome = centro_treinamento_nome))).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail=f'O Centro de Treinamento {centro_treinamento_nome} não foi encontrado'
        )
    
    try:
        atleta_out = AtletaSchemaOut(id=uuid4(), created_at= datetime.now(timezone.utc), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))
        
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        
        db_session.add(atleta_model)
        await db_session.commit()
    
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro ao inserir os dados no banco. {str(e)}'
        )
    return atleta_out

# GET ALL
@router.get(
    path='/',
    summary='Consultar todos os atletas registrados',
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaSchemaListOut]
)
async def query( # type: ignore
        db_session: DatabaseDependency,
        nome: Optional[str] = Query(default=None, description="Filtrar por nome"),
        cpf: Optional[str] = Query(default=None, description="Filtrar por CPF")
    )-> list[AtletaSchemaListOut]: # type: ignore 

    stmt = select(AtletaModel).options(
        selectinload(AtletaModel.centro_treinamento),
        selectinload(AtletaModel.categoria)
    )
    
    if nome:
        stmt = stmt.filter(AtletaModel.nome.ilike(f'{nome}'))
    
    if cpf:
        stmt = stmt.filter(AtletaModel.cpf == cpf)

    result =  await db_session.execute(stmt)
    atletas = result.scalars().all()
    
    return [
        AtletaSchemaListOut(
            nome=atleta.nome,
            centro_treinamento=CentroTreinamentoSchemaAtleta(nome=atleta.centro_treinamento.nome),
            categoria=CategoriaSchemaIn(nome=atleta.categoria.nome)
        )
        for atleta in atletas
    ]

  
    
# GET BY ID
@router.get(
    path='/{id}',
    summary='Consultar atleta pelo Id',
    status_code= status.HTTP_200_OK,
    response_model=AtletaSchemaOut
)
async def query(id: UUID, db_session: DatabaseDependency) -> AtletaSchemaOut: # type: ignore
    
    atleta: AtletaSchemaOut = (await db_session.execute(select(AtletaModel).filter_by(id = id))
                               ).scalars().first() # type:ignore
    
    if not atleta:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado para o id: {id}'
        )    
    return atleta

# UPDATE
@router.patch(
    path='/{id}',
    summary='Editar atleta pelo Id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaSchemaOut
)
async def query(id:UUID, db_session:DatabaseDependency, atleta_up:AtletaSchemaUpdate = Body()) -> AtletaSchemaOut: # type: ignore
    atleta: AtletaSchemaOut = (await db_session.execute(select(AtletaModel).filter_by(id = id))).scalars().first() # type: ignore
    
    if not atleta:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado para o id: {id}'
        )
    
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)
    
    return atleta
    
# DELETE
@router.delete(
     path='/{id}',
    summary='Remover atleta pelo Id',
    status_code=status.HTTP_204_NO_CONTENT
)
async def query(id: UUID, db_session: DatabaseDependency) -> None: # type:ignore
    atleta: AtletaSchemaOut = (await db_session.execute(select(AtletaModel).filter_by(id = id))).scalars().first() # type:ignore
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado para o id: {id}'
        )
        
    await db_session.delete(atleta)
    await db_session.commit()