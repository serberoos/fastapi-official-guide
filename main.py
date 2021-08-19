"""
필수 쿼리 매개변수
essential query parameter level 1
경로가 아닌 매개변수에 대한 기본값을 선언할 때
특정값을 추가하지 않고 선택적으로 만들기 위해서 기본값을 None으로 설정하면 되었지만

쿼리 매개변수를 필수로 만들려면 기본값을 선언할 수 없다.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}  # 쿼리 매개변수의 기본값을 선언하지 않으면 필수가 된다.
    return item
#needy는 필수 매개변수 이므로 반드시 URL에 설정해주어야한다.