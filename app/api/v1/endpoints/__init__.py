# app/api/v1/endpoints/__init__.py
from fastapi import APIRouter
from . import user, article  # 导入同级目录下的模块

# 创建一个总的 v1 路由实例
api_router = APIRouter()

# 汇总子路由
# 注意：这里假设你在 user.py 和 article.py 里的变量名都叫 router
api_router.include_router(user.router, prefix="/users", tags=["user model"])
api_router.include_router(article.router, prefix="/articles", tags=["article model"])