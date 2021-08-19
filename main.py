from fastapi import FastAPI

app = FastAPI()

"""
    POST : 데이터 생성
    GET : 데이터 읽기
    PUT : 데이터 업데이트
    DELETE : 데이터 삭제
"""

# 파이썬 포맷 문자열이 사용하는 동일한 문법으로 "매개 변수" 또는 "변수"를 경로에 선언할 수 있다.
@app.get("/items/{item_id}")
async def read_item(item_id):  # 경로 매개변수 item_id의 값은 함수의 item_id 인자로 전달된다.
    return {"item_id":item_id}
