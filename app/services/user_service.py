from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func
from app.models.user import User, UserStatus
from app.schemas.user import UserCreate, UserLogin
from app.core.security import PasswordHelper, create_access_token
from fastapi import HTTPException, status


async def create_user(db: AsyncSession, user_in: UserCreate):
    # 1. 检查用户是否存在
    result = await db.execute(select(User).where(User.name == user_in.name))
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    # 2. 哈希处理
    hashed_pwd = PasswordHelper.hash_password(user_in.password)

    # 3. 创建 Model 对象并存库
    new_user = User(
        name=user_in.name,
        hash_password=hashed_pwd,
        role="admin"  # 默认角色
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


# 处理用户登录认证
async def authenticate(db: AsyncSession, user_in: UserLogin, ip: str):
    result = await db.execute(select(User).where(User.name == user_in.name))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user does not exist"
        )

    is_valid = (
        not user.is_deleted and
        user.status == UserStatus.ACTIVE and
        PasswordHelper.verify_password(user_in.password, user.hash_password)
    )

    if is_valid:
        user.last_login_ip = ip
        user.login_failure_count = 0
    else:
        user.login_failure_count += 1
        if user.login_failure_count >= 16:
            user.status = UserStatus.DISABLE
        await db.commit()
        raise HTTPException(status_code=401, detail="Invalid credentials")

    await db.commit()
    return user


async def login_access_token(db: AsyncSession, user_in: UserLogin, ip: str):
     user = await authenticate(db, user_in, ip)

     token_data = {"sub": str(user.id), "role": user.role}
     access_token = create_access_token(data=token_data)

     return {
         "access_token": access_token,
         'token_type': "bearer"
     }


# 查询函数
async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()