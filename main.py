
# 첫째로 pydantic의 BaseModel을 import 해야 한다.
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel  # import pydantic's BaseModel


class Item(BaseModel):  # Create your data model : BaseModel을 상속 받는 데이터 모델 클래스 선언
    # 모든 속성 타입을 위해 파이썬 정규문법을 사용한다.
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None




app = FastAPI()

@app.post("/items/") # request body에 담아서 보내기
async def create_item(item: Item): # 매개변수로 선언
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax # 함수 내에서 모델 객체의 모든 속성에 직접 액세스 할 수 있다.
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

