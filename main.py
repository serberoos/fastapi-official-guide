"""
선택적 매개변수 Optional Parameter
같은 방법으로 기본값을 None으로 설정하여 선택적 매개변수를 선언할 수 있다.
"""
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False): # bool형으로 선언할 수도 있다.
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short: # short 값이 있는가 없는가를 bool로 판단한다.
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item