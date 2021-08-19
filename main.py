"""
경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언할 때, "쿼리 매개변수로 자동해석한다.
"""
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

"""
URL의 일부이므로 문자열이다.
파이썬 타입과 함께 선언할 경우 해당 타입으로 변환되고 검증한다.
"""


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):  # 쿼리 매개변수는 (default)기본값을 가질 수 있다.
    return fake_items_db[skip: skip + limit] # skip과 limit 퀴리 매개변수를 통해 출력되고 출력되지 않는다.

# 쿼리는 URL에서 ? 후에 나오고 &으로 구분되는 키-값의 쌍의 집합이다.
# 예를 들어 url에서 http://127.0.0.1:8000/items/?skip=0&limit=10
# skip - 값 0을 가진다.
# limit - 값 10을 가진다.
