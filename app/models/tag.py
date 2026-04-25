from datetime import datetime
from sqlalchemy import String, BigInteger, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, Relationship, relationship
from app.core.database import Base
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .article import Article

"""
Mapped[] 和 mapped_column 可以看作是 Python 和 MySQL 之间的映射
Mapped[] 是代码层：类型安全、IDE 补全
mapped_column 是存储层：约束、默认值、索引
"""

class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment='序号')

    tag_name: Mapped[str] = mapped_column(String(16), unique=True, nullable=False, comment='标签名')

    gmt_create: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='创建时间')

    gmt_modified: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment='修改时间'
    )

    # 对象关联
    # 当你看到一个标签时，请通过中间表去帮我把所有关联的文章找出来
    articles: Mapped[List["Article"]] = relationship(
        "Article",
        secondary="article_tag",  # 指明中间表
        back_populates="tags"  # 指向对方类(Article)中定义的属性名, 即在 Article 类中的 tags 属性
    )