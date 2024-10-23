from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from .base import Base


class User(Base, SQLAlchemyBaseUserTable[int]):
    pass
