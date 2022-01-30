import asyncio
import typing
from contextlib import asynccontextmanager

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import (AsyncSession, async_scoped_session, create_async_engine)
from sqlalchemy.orm import sessionmaker, declarative_base

from fishfry import base

Base = declarative_base()

_async_engine = create_async_engine(base.config.DB_URI, future=True)
_async_session_factory = sessionmaker(_async_engine, class_=AsyncSession, expire_on_commit=False)

_get_session = async_scoped_session(_async_session_factory, scopefunc=asyncio.current_task)

@asynccontextmanager
async def atomic_session() -> typing.AsyncIterator[AsyncSession]:
    async with _get_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

class Boat(Base):
    __tablename__ = 'boat'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
