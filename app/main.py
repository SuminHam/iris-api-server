from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Header
from starlette.concurrency import run_in_threadpool

from app import routers
from app.core.model_registry import model_registry
from app.utils import load_model, reload_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    model = await run_in_threadpool(load_model)
    model_registry.register_model("iris_model", model)

    yield

    model_registry.clear()


app = FastAPI(lifespan=lifespan)

app.include_router(routers.router)


@app.get("/healthcheck")
async def healthcheck():
    return "status:" "ok"
