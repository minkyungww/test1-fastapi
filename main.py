from fastapi import FastAPI
from pydantic import BaseModel

class Cat(BaseModel):
    name:str
    id: int

app = FastAPI()

# passvaluable: /주소/매개변수
@app.get("/first/{id}") # get은 rest 통신 방식 중 하나, /는 기본주소를 뜻함, 뒤에 다른 텍스트를 추가하면, 주소창에도 /first라고 추가해줘야함
async def root(id:int): #아래 코드를 실행
    return {"message": "Hello World", "id": id} #프레임워크가 객체를 알아서 json로 만들어줌, return에는 무조건 문자형이 와야함(?)

# querystring: /주소?key=value&key=value
@app.get("/second")
async def second(skip: int = 0, limit: int = 10): #쿼리 매개변수
    return {"skip":skip, "limit":limit} #주소에 값을 지정안하면 위 기본값이 출력됨; 딕션너리 {불변데이터:값}

@app.post("/cat")
async def cat(cat: Cat):
    return cat

