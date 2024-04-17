from contextlib import asynccontextmanager
from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.concurrency import run_in_threadpool

from app import routers
from app.core.model_registry import model_registry
from app.core.middlewares.metric_middleware import MetricMiddleware
from app.utils import load_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    model = await run_in_threadpool(load_model)
    model_registry.register_model("iris_model", model)

    yield

    model_registry.clear()


app = FastAPI(lifespan=lifespan)

app.include_router(routers.router)
app.add_middleware(MetricMiddleware)


@app.get("/healthcheck")
async def healthcheck():
    return "status:" "ok"


@app.get("/metrics")
async def get_metrics():
    headers = {"Content-Type": CONTENT_TYPE_LATEST}
    content = generate_latest().decode("utf-8")
    return Response(content=content, media_type="text/plain", headers=headers)
