from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import String, BigInteger, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from .article import Article

class Attachment(Base):
    __tablename__ = "attachment"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="序号")
    object_key: Mapped[str] = mapped_column(String(255), nullable=False, comment="MinIO路径")
    bucket: Mapped[str] = mapped_column(String(64), nullable=False, comment="存储桶名称")
    file_size: Mapped[int] = mapped_column(BigInteger, comment="文件大小") # 注意这里是 int
    mime_type: Mapped[str] = mapped_column(String(32), comment="文件类型")

    article_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("article.id"), nullable=False)
    # 逻辑外键
    article: Mapped["Article"] = relationship("Article", back_populates="attachments")

    gmt_create: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="创建时间")
    gmt_modified: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment="修改时间"
    )