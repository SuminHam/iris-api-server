from fastapi import APIRouter

from app.routers import ml_router

router = APIRouter()

router.include_router(ml_router.router,
                      prefix="/v1/ml",
                      tags=['ml'])