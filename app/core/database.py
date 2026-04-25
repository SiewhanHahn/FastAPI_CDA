# 定义 Base 基类
"""
Base 类通常通过 DeclarativeBase 创建。
它就像一个容器，当你运行数据库迁移（Alembic）时，
它会扫描所有继承自它的子类，从而知道要创建哪些表。
"""


import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator
from dotenv import load_dotenv


# 加载 .env 文件
load_dotenv()


# 从环境变量获取数据库地址
DATABASE_URL = os.getenv("DATABASE_URL")


# 定义基类
class Base(DeclarativeBase):
    pass

# 创建异步引擎
# echo = True 在控制台打印所有生成的原始 SQL
engine = create_async_engine(DATABASE_URL, echo=True)


# 异步会话工厂
"""
expire_on_commit
这个参数控制的是 SQLAlchemy 对象的生命周期。
默认状态 (True)：
    当你执行 commit() 时，SQLAlchemy 认为数据库里的数据已经变了，所以它会把内存里对象的属性（比如 user.name）全部“抹除”标记为过期。
    如果你之后想看 user.name，它会发现数据没了，然后偷偷发一条 SQL 去数据库再查一遍。
异步痛点：
    在异步代码里，所有的查库操作必须显式地写 await。这种“偷偷查库”的操作没有 await，会导致程序直接崩溃。
expire_on_commit=False：
    告诉 SQLAlchemy：“事务提交后，别动我内存里的数据。即便数据库变了，我也先用着内存里的旧快照，不许偷偷查库。”
"""
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    # 在异步中，提交事务后对象如果不保持活动状态
    # 再次访问属性会触发自动加载（这在异步中是禁止的）
    expire_on_commit=False
)




async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    异步数据会话生成器
    每一个请求会自动创建一个 session，处理完后自动关闭
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()