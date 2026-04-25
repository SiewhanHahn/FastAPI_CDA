from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import String, BigInteger, DateTime, func, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from .user import User
    from .attachment import Attachment
    from .tag import Tag

class Article(Base):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False, comment="标题")
    content: Mapped[str] = mapped_column(Text, nullable=False, comment="Markdown内容")  # 改为 Text 类型
    summary: Mapped[str | None] = mapped_column(String(256), comment="摘要")

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("user.id"), nullable=False)

    gmt_create: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    gmt_modified: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # 逻辑外键：指向类名 "User", 一篇文章关联一个作者
    author: Mapped["User"] = relationship("User", back_populates="articles")

    # 逻辑外键：一篇文章可以有多个附件
    attachments: Mapped[List["Attachment"]] = relationship("Attachment", back_populates="article")

    # 多对多关联: 通过 article_tag 表找到 Tag
    tags: Mapped[list["Tag"]] = relationship(
        "Tag",
        secondary="article_tag",
        back_populates="articles"
    )