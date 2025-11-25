from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health", status_code=200)
def health_check():

    return {
        "status": "ok",
        "dttm": today.starttime("%Y-%m-%d %H:%M:%S")
    }