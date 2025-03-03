from fastapi import FastAPI
from . import models, schemas
from .database import engine
from .routers import racers, ranks

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    racers.router
)
app.include_router(ranks.router)