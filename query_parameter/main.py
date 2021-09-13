"""
필수 쿼리 매개변수
essential query parameter level 1
경로가 아닌 매개변수에 대한 기본값을 선언할 때
특정값을 추가하지 않고 선택적으로 만들기 위해서 기본값을 None으로 설정하면 되었지만

쿼리 매개변수를 필수로 만들려면 기본값을 선언할 수 없다.
"""
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
"""
경로 매개변수 - item_id

쿼리 매개변수 
- needy (필수)
- skip (기본값=0)
- limit (선택 매개변수 : 기본값 None)
"""

# 팁 : 경로 매개변수와 마찬가지로 Enum을 사용할 수 있다.