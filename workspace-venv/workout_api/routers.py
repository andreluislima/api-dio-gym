from fastapi import APIRouter
from workout_api.centro_treinamento.centro_treinamento_controller import router as centro_treinamento
from workout_api.categoria.categoria_controller import router as categorias

api_router = APIRouter()

api_router.include_router(centro_treinamento, prefix='/centro_treinamento', tags=['centro_treinamento'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
