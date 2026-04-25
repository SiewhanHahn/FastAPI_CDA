from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.schemas.user import UserOut

# 基础模型
class ArticleBase(BaseModel):
    title: str
    content: str
    summary: Optional[str] = None


# 创建文章时传入参数
class ArticleCreate(ArticleBase):
    id: int
    user_id: int
    gmt_create: datetime
    gmt_modified: datetime

    class Config:
        from_attributes = True  # 允许兼容 SQLAlchemy 对象


# 文章输出时的传出参数
class ArticleOut(ArticleBase):
    id: int
    user_id: int
    gmt_create: datetime
    gmt_modified: datetime


# 展示文章详情
class ArticleWithAuthor(ArticleBase):
    author: UserOut  # 此处对应 Article Model 中的 author relationship

    class Config:
        from_attributes = True