"""
선택적 매개변수 Optional Parameter
같은 방법으로 기본값을 None으로 설정하여 선택적 매개변수를 선언할 수 있다.
"""
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id : str, q : Optional[str] = None): # 매개변수 q는 선택적이며 기본값으로 None값이 된다.
    # 자료형 쓰는 곳에 Optional[str] 형식으로 작성한다. - 기본값은 None
    if q: # q가 존재하면 매개변수 q도 같이 response한다.
        return {"item_id":item_id, "q":q}
    return {"item_id":item_id}