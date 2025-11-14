from fastapi import FastAPI

# FastAPI 문서 페이지 경로를 /api/docs, 
# 스펙 JSON 경로를 /api/openapi.json으로 지정하는 설정.
app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

@app.get("/hello")
def say_hello() -> dict:
    """간단한 JSON 메시지를 반환합니다."""
    return {"message": "Hello, FastAPI learners!"}

if __name__ == "__main__":
    # uv run uvicorn --reload --port=8888 examples.hour01.01_hello_fastapi:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)