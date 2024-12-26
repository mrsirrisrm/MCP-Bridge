from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from ..config import config

SessionMaker = async_sessionmaker()

async def configure_database():
    engine = create_async_engine(
        config.database.url,
        echo=config.database.echo,
    )
    SessionMaker.configure(bind=engine)

async def get_session():
    db = SessionMaker()
    try:
        yield db
    finally:
        await db.close()