# infrastructure/database.py
#from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import os


from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from domain.contacts.ports import ContactRepositoryPort
from collections.abc import AsyncGenerator

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/contact_db"
)
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session

