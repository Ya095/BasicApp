import contextlib
import asyncio

from fastapi_users.exceptions import UserAlreadyExists
from sqlalchemy.util import await_only

from api.dependencies.authentication.users import get_user_db
from core.authentication.user_manager import UserManager
from core.models import db_helper, User
from core.schemas.user import UserCreate
from api.dependencies.authentication.user_manager import get_user_manager


# get_async_session_context = contextlib.asynccontextmanager(db_helper.session_getter())
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = "admin@admin.com"
default_password = "abc"
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    try:
        async with db_helper.session_factory() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    return await create_user(
                        user_manager,
                        user_create
                    )
    except UserAlreadyExists:
        print(f"User {email} already exists")
        raise


if __name__ == '__main__':
    asyncio.run(create_superuser())