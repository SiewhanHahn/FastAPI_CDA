"""
从请求头里提取 Token -> 验证它 -> 从数据库里把这个用户取出来
"""

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
import os

from app.core.database import get_db
from app.services import user_service
from app.models.user import User


# 定义 Token 的获取方式： 从 Authorization：Bearer <TOKEN> 头部获取
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/user/login")


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


async def get_current_user(
        db: AsyncSession = Depends(get_db),
        token: str = Depends(oauth2_scheme),
) -> User:
    """
    权限拦截器：验证 Token 并返回当前登陆的用户实例
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # 解码 Token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 3. 根据 Token 里的 ID 去数据库查人
    # 这里我们直接复用 Service 层逻辑
    user = await user_service.get_user_by_id(db, user_id=int(user_id))

    if user is None:
        raise credentials_exception

    return user