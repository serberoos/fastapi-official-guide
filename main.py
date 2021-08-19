from fastapi import FastAPI
# API에 대한 모든 기능을 제공하는 파이썬 클래스 FastAPI
# Starlette를 직접 상속하는 클래스로 Starlette의 모든 기능을 사용가능하다.

app = FastAPI() #FastAPI 클래스의 인스턴스
# uvicorn main:fastapi --reload

"""
    POST : 데이터 생성
    GET : 데이터 읽기
    PUT : 데이터 업데이트
    DELETE : 데이터 삭제
"""

@app.get("/") # 경로는 첫번째 / 에서 시작하는 URL의 마지막 부분이다.
# get동작을 사용하여 URL "/"에 대한 요청을 받을 때마다 FastAPI에 의해 호출된다.
async def root(): # / 경로가 실행될때 실행하는 함수 , async는 비동기 형식
    return {"message":"Hello World"} # dict, list 단일값을 가진 str int 등을 반환 할 수 있다.
