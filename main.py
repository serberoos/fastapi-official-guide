from fastapi import FastAPI

app =FastAPI()

@app.get("/users/me") # 이건 고정경로
async def read_user_me():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}") # 이건 매개변수 경로
async def read_user(user_id: str):
    return {"user_id" : user_id}

"""
    고정 경로와 매개변수 경로가 같이 있으면 고정 경로를 먼저 선언하고 후에 매개변수 경로를 선언해야한다.
    /users/{user_id} 이전에 /users/me를 선언해야한다.
    
    그렇지 않으면 /users/{user_id} 는 매개변수 user_id의 값을 me라고 생각하여 /users/me도 연결한다.
"""