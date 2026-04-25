from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.article import ArticleCreate, ArticleOut
from app.services import article_service

router = APIRouter()

@router.post("/", response_model=ArticleOut)
async def create_new_article(
        article_in: ArticleCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)  # 身份校验：不登录不准发
):
    """
    发布新文章（受保护接口）
    """
    return await article_service.create_article(
        db=db,
        article_in=article_in,
        owner_id=current_user.id  # 从 Token 解析出来的 ID
    )

@router.get("/", response_model=List[ArticleOut])
async def read_articles(
        db: AsyncSession = Depends(get_db),
        skip: int = 0,  # 默认从第 0 条开始
        limit: int = 10,  # 默认取 10 条
):
    """
    公开接口：获取文章列表
    """
    return await article_service.get_articles(
        db=db,
        skip=skip,
        limit=limit
    )