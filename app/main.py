from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import api_router

app = FastAPI(title="Ryan's API")

# 配置 CORS 跨域策略 (信安专业重点：最小权限原则，不要用 "*")
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # 允许访问的源
    allow_credentials=True,      # 支持 cookie 等凭证
    allow_methods=["*"],         # 允许的请求方法 (GET, POST, etc.)
    allow_headers=["*"],         # 允许的请求头 (包含 Authorization)
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Ryan's API"}