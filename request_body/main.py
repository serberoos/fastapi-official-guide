"""
Request body + path parameters + query parameter

body path query를 동시에 선언할 수 있다.
fastapi는 각각을 인식하고 올바른 위치에서 데이터를 가져온다.
"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description : Optional[str] = None
    price :float
    tax :Optional[float] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id:int, item:Item, q:Optional[str] = None):
    result = {"item_id":item_id, **item.dict()}
    if q:
        result.update({"q":q})
    return result

"""
    함수 매개변수는 다음처럼 인식됩니다.
    - 매개변수가 경로에서도 선언되면 경로 매개변수로 사용된다.
    - 매개변수가 단일 유형(ex int:float,str,bool 등)인경우 쿼리 매개변수로 해석된다.
    - 매개변수가 pydantic 모델 유형으로 선언되면 요청본문으로 해석된다.
"""