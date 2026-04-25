"""
定义数据契约：
由于数据库模型（Model）包含敏感字段（如 hash_password），
开发者绝不能直接把 Model 返回给前端。我们需要使用 Pydantic 定义“入参”和“出参”。
"""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

# 注册时的传入参数：用户只传输明文密码
class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=16)
    password: str = Field(..., min_length=4, max_length=16)
    pass


# 返回给前端的信息：绝对不能包含密码哈希
class UserOut(BaseModel):
    id: int
    name: str
    role: str
    gmt_create: datetime

    # 核心配置：允许 Pydantic 读取 SQLAlchemy 的 ORM 模型对象
    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    name: str = Field(..., min_length=1, max_length=16)
    password: str = Field(..., min_length=4, max_length=16)
    pass


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

