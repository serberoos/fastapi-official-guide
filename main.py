from enum import Enum
from fastapi import FastAPI
"""
Enum 열거형을 이용한 사전 정의 값

"""

class ModelName(str, Enum): # string enum
    alexnet ="alexnet"
    resnet = "resnet"
    lenet = "lenet"
# 값은 3개 중 1개가 들어가야함 안그럼 오류
app =FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet: #모델이름이 알렉스넷
        return {"model_name": model_name, "message" : "Deep Learning FTW!"}

    if model_name.value == "lenet": #모델이름 값이 lenet
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name ": model_name, "message":"Have some residuals"} # resnet