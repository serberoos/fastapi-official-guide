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
async def read_item(item_id : int):  # 경로 매개변수 item_id의 값은 함수의 item_id 인자로 전달된다.
    return {"item_id":item_id} # 파이썬 표준 타입 어노테이션을 이용해 함수의 경로 매개변수의 타입을 선언할 수 있다.
# 이 상태에서 매개변수가 int형이 아니라면 오류 발생

""" 
    다양한 도구가 존재한다.
    Pydantic - 모든 데이터 검증은 내부적으로 수행되고 이로 인해 이득을 얻는다.
"""
