from fastapi import FastAPI
from workout_api.routers import api_router
from workout_api.relationships_init import init_relationships

app = FastAPI(title="WorkoutApi")
app.include_router(api_router)
init_relationships()

# if __name__ == 'main':
#     import uvicorn

#     uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
#     # uvicorn workout_api.main:app --reload
