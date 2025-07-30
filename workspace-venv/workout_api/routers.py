from fastapi import APIRouter
from workout_api.centro_treinamento.centro_treinamento_controller import router as centro_treinamento
from workout_api.categoria.categoria_controller import router as categoria
from workout_api.atleta.atleta_controller import router as atleta

api_router = APIRouter()

api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centro_treinamento', tags=['centro_treinamento'])
