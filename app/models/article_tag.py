from datetime import datetime
from sqlalchemy import BigInteger, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class ArticleTag(Base):
    __tablename__ = "article_tag"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment='序号')

    # 关联文章
    article_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("article.id"), nullable=False, comment="文章ID")

    # 关联标签
    tag_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("tag.id"), nullable=False, comment="标签ID")

    # 审计字段
    gmt_create: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="创建时间")

    gmt_modified: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="修改时间"
    )