"""
Request body + path parameters
requestbody와 path parameter를 동시에 선언할 수 있다.
fastapi는 경로 매개변수와 일치하는 함수 매개변수를 경로에서 가져와야한다.
그리고 Pydantic모델로 선언된 함수 매개변수를 request body에서 가져와야한다는 것을 인지한다.
"""
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price :float
    tax : Optional[float] = None

app =FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item:Item):
    return {"item_id":item_id, **item.dict()}