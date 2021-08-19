"""
여러 경로/쿼리 매개변수
multiple path and query parameter

경로 매개변수와 쿼리 매개변수를 동시에 선언할 수 있고 fastAPI는 어느것이 무엇인지 알고 있다.
그리고 특정 순서로 선언할 필요없다.

매개변수들은 이름으로 감지된다.
"""
from typing import Optional
from fastapi import FastAPI

app =FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id:str, q: Optional[str] = None, short: bool = False):
    item = {"item_id":item_id, "owner_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is an amazing item that has a long description"})
    return item
