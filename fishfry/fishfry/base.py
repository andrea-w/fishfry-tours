import os
import re
import typing

class Config:
    DB_URI = os.getenv('DATABASE_URL')
    if DB_URI.startswith("postgres://"):
        DB_URI = DB_URI.replace("postgres://", "postgresql+asyncpg://", 1)

    def __init__(self, prefix: str = "FISHFRY_"):
        for name, type_ in typing.get_type_hints(self).items():
            envname = prefix + name
            if envname in os.environ:
                setattr(self, name, type_(os.environ[envname]))


config = Config()