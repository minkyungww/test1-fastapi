from fastapi import FastAPI

app = FastAPI()


@app.get("/first") # get은 rest 통신 방식 중 하나, /는 기본주소를 뜻함, 뒤에 다른 텍스트를 추가하면, 주소창에도 /first라고 추가해줘야함
async def root(): #아래 코드를 실행
    return {"message": "Hello World"} #프레임워크가 객체를 알아서 json로 만들어줌, return에는 무조건 문자형이 와야함(?)

