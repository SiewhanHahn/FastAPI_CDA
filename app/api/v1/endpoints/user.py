from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas.user import UserCreate, UserOut
from app.services import user_service
from app.core.database import get_db
from app.schemas.user import UserLogin, Token
from app.api.deps import get_current_user


router = APIRouter()

@router.post("/register", response_model=UserOut, summary="Register a new user")
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # 调用 service 层的逻辑
    return await user_service.create_user(db, UserCreate(**user.model_dump()))


"""
# 用户登录，捕获IP
@router.post("/login")
async def login(
        user_in: UserLogin,
        request: Request,
        db: AsyncSession = Depends(get_db)
):
    # 提取 IP 地址：优先看是否存在代理转发，没有则获取 host
    ip = request.headers.get("X-Forwarded-For") or request.client.host
    # 传给 Service 处理业务逻辑
    return await user_service.authenticate(db, user_in, ip)

"""
@router.post("/login", response_model=Token)
async def login_for_access_token(
        user_in: UserLogin,
        request: Request,
        db: AsyncSession = Depends(get_db)
):
    # 提取 IP
    ipaddress = request.client.host

    # 直接返回结果（FastAPI 会根据 Token Schema 自动序列化）
    return await user_service.login_access_token(db, user_in, ipaddress)


@router.get("/me", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user