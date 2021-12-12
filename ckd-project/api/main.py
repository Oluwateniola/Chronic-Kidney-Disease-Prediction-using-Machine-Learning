from fastapi import FastAPI, Body, Header, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from api.model.utils import Data
from api.model.preprocess import predict_response
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/predict", status_code=HTTP_200_OK)
async def predict(request: Data):
    dictData = request.dict()
    response = predict_response(dictData)
    return response

"""if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="info")"""