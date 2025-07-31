from fastapi import FastAPI
from workout_api.routers import api_router
from workout_api.relationships_init import init_relationships
from fastapi_pagination import add_pagination

app = FastAPI(title="WorkoutApi")

# Registra rotas
app.include_router(api_router)

# Configura paginação
add_pagination(app)

# Inicializa relacionamentos (evita import circular)
init_relationships()


