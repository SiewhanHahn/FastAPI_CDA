# app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints import api_router  # 明确导入 api_router 实例

app = FastAPI(title="Ryan's API")

# 将汇总好的路由挂载到总路径下
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Ryan's API"}