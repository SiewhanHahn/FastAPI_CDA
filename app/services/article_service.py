from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.article import Article
from app.schemas.article import ArticleCreate


async def create_article(db: AsyncSession, article_in: ArticleCreate, owner_id: int) -> Article:
    # 组装实例模型，强制注入 owner_id
    new_article = Article(
        title=article_in.title,
        content=article_in.content,
        summary=article_in.summary,
        user_id=owner_id,  # 权限隔离，不信任前端传的 ID
    )

    # 库存
    db.add(new_article)
    await db.commit()
    await db.refresh(new_article)
    return new_article

async def get_articles(db: AsyncSession, skip: int = 0, limit: int = 100):
    """
    简单查询：获取文章列表
    :param skip: 跳过多少条（用于分页）
    :param limit: 取多少条
    """
    # 构造 SQL: select * from article limit 10 offset 0
    query = select(Article).offset(skip).limit(limit)
    result = await db.execute(query)

    # scalars().all() 会把查询结果里的每一行包装成 Article 对象并存入列表
    return result.scalars().all()