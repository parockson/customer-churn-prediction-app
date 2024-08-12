import sys
import os

# Add src to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.coder import PickleCoder
from fastapi_cache.decorator import cache
import uvicorn
from redis import asyncio as aioredis
from pydantic import BaseModel
from typing import Tuple, Dict, Union
from imblearn.pipeline import Pipeline as imbPipeline
from sklearn.preprocessing._label import LabelEncoder
import joblib
import pandas as pd
from urllib.request import urlopen
from src.config import ONE_DAY_SEC, ONE_WEEK_SEC, LGBM_URL, XGBClassifier_URL, RandomForest_URL, ENCODER_URL, ENV_PATH
from dotenv import load_dotenv
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager


load_dotenv()

# API input features
class ChurnFeatures(BaseModel):
    REGION: str
    Tenure: float
    Recharge_Amount: float
    FREQUENCE_RECH: float
    REVENUE: float
    ARPU_SEGMENT: str
    FREQUENCE: float
    DATA_VOLUME: float
    ON_NET: float
    ORANGE: float
    TIGO: float
    REGULARITY: float
    TOP_PACK: str
    FREQ_TOP_PACK: float


class Url(BaseModel):
    pipeline_url: str
    encoder_url: str


class ResultData(BaseModel):
    prediction: str
    probability: float


class PredictionResponse(BaseModel):
    execution_msg: str
    execution_code: int
    result: ResultData


class ErrorResponse(BaseModel):
    execution_msg: Union[str, None]
    execution_code: Union[int, None]
    result: Union[Dict[str, Union[str, int]], Union[Dict[str, None], None]]


# Load the model pipelines and encoder
# Cache for 1 day
@cache(expire=ONE_DAY_SEC, namespace='pipeline_resource', coder=PickleCoder)
async def load_pipeline(pipeline_url: str, encoder_url: str) -> Tuple[imbPipeline, LabelEncoder]:
    pipeline, encoder = None, None
    try:
        pipeline: imbPipeline = joblib.load(urlopen(pipeline_url))
        encoder: LabelEncoder = joblib.load(urlopen(encoder_url))
    except Exception:
        # Log exception
        pass
    finally:
        return pipeline, encoder


# Endpoints
app = FastAPI()

@app.get('/')
async def status_check():
    return {"Status": "API is online..."}


#@cache(expire=ONE_DAY_SEC, namespace='pipeline_classifier')  # Cache for 1 day
async def pipeline_classifier(pipeline: imbPipeline, encoder: LabelEncoder, data: ChurnFeatures) -> ErrorResponse | PredictionResponse:
    output = ErrorResponse(**{'execution_msg': None,
                              'execution_code': None, 'result': None})
    try:
        # Create dataframe
        df = pd.DataFrame([data.dict()])

        # Make prediction
        prediction = pipeline.predict(df)

        pred_int = int(prediction[0])

        prediction = encoder.inverse_transform([pred_int])[0]

        # Get the probability of the predicted class
        probability = round(
            float(pipeline.predict_proba(df)[0][pred_int] * 100), 2)

        msg = 'Execution was successful'
        code = 1
        result = {"prediction": prediction, "probability": probability}

        output = PredictionResponse(
            **{'execution_msg': msg,
               'execution_code': code, 'result': result}
        )

    except Exception as e:
        msg = 'Execution failed'
        code = 0
        result = {'error': f"Omg, pipeline classifier failure: {e}'"}
        output = ErrorResponse(**{'execution_msg': msg,
                                  'execution_code': code, 'result': result})

    finally:
        return output


# LGBM endpoint: classify churn with xgboost
@app.post('/LGBM_prediction')
async def LGBM_Classifier(data: ChurnFeatures) -> ErrorResponse | PredictionResponse:
    xgboost_pipeline, encoder = await load_pipeline(LGBM_URL, ENCODER_URL)
    output = await pipeline_classifier(xgboost_pipeline, encoder, data)
    return output


# XGBoost endpoint: classify churn with random forest
@app.post('/XGBoost_prediction')
async def XGB_Classifier(data: ChurnFeatures) -> ErrorResponse | PredictionResponse:
    random_forest_pipeline, encoder = await load_pipeline(XGBClassifier_URL, ENCODER_URL)
    output = await pipeline_classifier(random_forest_pipeline, encoder, data)
    return output


# RandomForest endpoint: classify churn with random forest
@app.post('/Random_Forest_prediction')
async def RandomForest_Classifier(data: ChurnFeatures) -> ErrorResponse | PredictionResponse:
    random_forest_pipeline, encoder = await load_pipeline(RandomForest_URL, ENCODER_URL)
    output = await pipeline_classifier(random_forest_pipeline, encoder, data)
    return output

# Your FastAPI routes and logic here

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


