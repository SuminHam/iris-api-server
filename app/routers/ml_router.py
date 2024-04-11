# app/routers/ml_router.py
import pandas as pd
from fastapi import APIRouter

from app.schemas.request import IrisReq
from app.schemas.response import ResponseModel, IrisResp
from app.core.model_registry import model_registry


router = APIRouter()


@router.post("/predict", response_model=ResponseModel)
def predict(request: IrisReq):
   result = model_registry.get_model("iris_model").predict(
       pd.DataFrame([request.model_dump()])
   )

   return ResponseModel(status_code=200, data=IrisResp(target=result))


