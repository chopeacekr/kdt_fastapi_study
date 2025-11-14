from fastapi import FastAPI, HTTPException
app = FastAPI(docs_url="/api/docs", redoc_url="/api/openapi.json")

ANSWER = {"greeting": "안녕하세요", "farewell": "다음에 또 만나요."}

def fetch_answer(intent: str) -> str:
    if intent not in ANSWER:
        raise HTTPException(status_code=404, detail=f"Intent '{intent}' not found")
    return ANSWER[intent]

@app.get("/answer/{intent}")
def answer_endpoint(intent: str) -> dict:
    return {"intent": intent, "answer": fetch_answer(intent)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)
