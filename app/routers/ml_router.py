# app/routers/ml_router.py
import pandas as pd
from fastapi import APIRouter, HTTPException, Header

from app.schemas.request import IrisReq
from app.schemas.response import ResponseModel, IrisResp
from app.core.model_registry import model_registry
from app.utils import (
    load_model,
    reload_model,
    get_current_model_version,
    get_production_model_version,
)

router = APIRouter()


@router.post("/predict", response_model=ResponseModel)
def predict(request: IrisReq):
    result = model_registry.get_model("iris_model").predict(
        pd.DataFrame([request.model_dump()])
    )

    return ResponseModel(status_code=200, data=IrisResp(target=result))


@router.post("/reload-model")
async def check_and_reload_model(x_api_key: str = Header(...)):
    current_version = get_current_model_version()
    production_version = get_production_model_version()
    if x_api_key != "74a92e812e39e294d0ac458bed76f2c621744a20a67e3e9bc2be8849e5efa6f3":
        raise HTTPException(status_code=401, detail="Unauthorized")

    await reload_model()
    return {"message": "Model reloaded successfully"}
