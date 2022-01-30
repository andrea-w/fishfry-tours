import asyncio
import dataclasses
from enum import auto
import typing
from contextlib import asynccontextmanager

from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.asyncio import (AsyncSession, async_scoped_session, create_async_engine)
from sqlalchemy.orm import sessionmaker, declarative_base, registry

from fishfry import base

# Base = declarative_base()
mapper_registry = registry()

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

# class Boat(Base):
@mapper_registry.mapped
@dataclasses.dataclass
class Boat:
    # __tablename__ = 'boat'

    # id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    # name = Column(String, nullable=False)
    # status = Column(String, nullable=False)
    __table__ = Table('boat', mapper_registry.metadata,
        Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
        Column("name", String, nullable=False, unique=True),
        Column("status", String, nullable=False))

    id: int = dataclasses.field(init=False)
    name: str
    status: str
