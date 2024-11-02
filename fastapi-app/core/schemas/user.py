from fastapi_users import schemas

from core.types.user_id import userIdType


class UserRead(schemas.BaseUser[userIdType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass