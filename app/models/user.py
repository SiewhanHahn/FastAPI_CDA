from datetime import datetime
from sqlalchemy import String, BigInteger, DateTime, func, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
import enum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .article import Article  # 仅用于类型检查，运行时不执行


class UserStatus(enum.IntEnum):
    """
    使用 IntEnum，数据库存储使用 tinyint，代码中使用枚举名
    """
    ACTIVE = 1
    DISABLE = 0
    pass


class User(Base):
    __tablename__ = "user"

    # 核心字段
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment='序号')

    name: Mapped[str] = mapped_column(String(16), unique=True, nullable=False, comment='昵称')

    hash_password: Mapped[str] = mapped_column(String(256), nullable=False, comment="哈希存储密码")

    role: Mapped[str] = mapped_column(String(16), nullable=False, comment="角色")

    status: Mapped[int] = mapped_column(SmallInteger, default=UserStatus.ACTIVE)

    # 安全字段
    last_login_ip: Mapped[str] = mapped_column(String(45), nullable=True, comment="最后登录的IP地址")

    is_deleted: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False, comment="逻辑删除")

    login_failure_count: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False, comment="登录失败次数")

    last_login_time: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="最后登录的时间")

    # 审计字段
    gmt_create: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="创建时间")

    gmt_modified: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="修改时间"
    )

    # 逻辑外键：一个用户对应多个文章，所以是 list
    # back_populates="author" 对应 Article 类里的属性名
    articles: Mapped["list[Article]"] = relationship("Article", back_populates="author")
