from fastapi import FastAPI

app =FastAPI()
"""
OpenAPI는 경로를 포함하는 경로 매개변수를 내부에 선언하는 방법을 지원하지 않는다.
지원
/files/{file_path:path}
이러한 경우 매개변수의 이름은 file_path이고 마지막 부분 : path는 매개변수가 경로와 일치해야함을 알려준다.
"""
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}