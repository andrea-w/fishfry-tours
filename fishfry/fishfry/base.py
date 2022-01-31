import os
import typing


class Config:
    # DB_URI: str = "postgresql+asyncpg://pgadmin:password@localhost/testdb"
    DB_URI: str = os.environ['DATABASE_URL']

    def __init__(self, prefix: str = "FISHFRY_"):
        for name, type_ in typing.get_type_hints(self).items():
            envname = prefix + name
            if envname in os.environ:
                setattr(self, name, type_(os.environ[envname]))


config = Config()