from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Sequence


# Заменить на свое
def return_something():
    return 1


# async def get_all_users(session: AsyncSession) -> Sequence[User]:
#     stmt = select(User).order_by(User.id)
#     results = await session.scalars(stmt)
#     return results.all()