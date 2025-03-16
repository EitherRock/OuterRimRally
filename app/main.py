from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth.views import router as auth_router
from .racer.views import router as racer_router
from .rank.views import router as rank_router
from .category.views import router as category_router
from .part.views import router as part_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(racer_router)
app.include_router(rank_router)
app.include_router(part_router)
app.include_router(category_router)
app.include_router(auth_router)