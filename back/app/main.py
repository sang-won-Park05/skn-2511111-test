from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="나의 멋진 API",
    description="이것은 내 FastAPI 애플리케이션의 설명입니다.",
    version="1.0.0"
)

@app.get("/health", status_code=200)
def health_check():
    return {
        "status": "ok",
        "dttm": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }