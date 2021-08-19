"""
클라이언트 브라우저로부터 API를 이용해 데이터를 전송하고자 할때 request body를 써야한다.
한개의 request body는 클라이언트가 API를 이용하여 보낸 데이터이고 서버가 API를 이용해 클라이언트에게 보낸 데이터다.
너의 API는 거의 항상 response body를 보내야한다. 그러나 고객은 항상 response body를 보낼 필요는 없다.
request body를 선언하기 위해 너는 Pydantic 모델을 사용해야 한다.

#info
데이터를 보내기위해 너는 POST(가장 흔함), PUT, DELETE or PATCH를 이용해야만 한다.
GET요청 하면서 request body를 보내는 것은 권장되지 않는다. 극단적인 경우 아니면 지원안함
"""

# 첫째로 pydantic의 BaseModel을 import 해야 한다.
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel  # import pydantic's BaseModel


class Item(BaseModel):  # Create your data model : BaseModel을 상속 받는 데이터 모델 클래스 선언
    # 모든 속성 타입을 위해 파이썬 정규문법을 사용한다.
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


"""
    퀴리 매개변수를 선언할 때와 마찬가지로 모델 속성에 기본값이 있는 경우에는 필요하지 않다. 하지만 기본값이 없다면 필수이다.
    None은 그냥 선택사항으로 만들기 위해 사용한다. None인 항목의 경우 값을 써주지 않아도 유효하다.
"""

app = FastAPI()

@app.post("/items/") # request body에 담아서 보내기
async def create_item(item: Item): # 매개변수로 선언
    return item

"""
    매개변수 클래스 Item을 item으로 선언하고 리턴
    
    # 결과
    단순한 파이썬 타입 선언 만으로 FastAPI는 다음을 수행한다.
    1. request의 body를 JSON으로 읽는다.
    2. 필요할 경우 형변환
    3. 만약 데이터가 사용불가할 경우 정확하고 명확한 오류를 반환
    4. 매개변수에 수신된 데이터를 제공한다.
    5. 모델에 대한 JSON 정의를 생성한다.
    6. 그러한 스키마는 생성된 OpenAPI 스키마의 일부이고 automatic documentation UI에서 사용된다.
    
    Automatic Docs
    모델의 JSON 스키마는 OpenAPI 생성 스키마의 일부이며 대화형 API 문서에 표시된다.
    또한 이를 필요로 하는 각 경로의 API 문서에서도 사용된다.
    
    
"""