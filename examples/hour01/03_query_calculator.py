from fastapi import FastAPI

# FastAPI 문서 페이지 경로를 /api/docs, 
# 스펙 JSON 경로를 /api/openapi.json으로 지정하는 설정.
app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

def add_numbers(a: float, b: float) -> dict:
    """두 수의 합과 차를 반환합니다."""
    return {"sum": a + b, "difference": a - b}

def greet_user(name: str) -> dict:
    """이름을 받아 환영 메시지를 만듭니다."""
    return {"message": f"Nice to meet you, {name}!"}

@app.get("/math/add")
def add_endpoint(a: float = 0.0, b: float = 0.0) -> dict:
    return add_numbers(a, b)

@app.get("/users/{name}")
def greet_endpoint(name: str) -> dict:
    return greet_user(name)

if __name__ == "__main__":
    # uv run uvicorn --reload examples.hour01.02_path_parameter:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)
    