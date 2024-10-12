from fastapi import APIRouter
from .crud.some_obj import return_something


router = APIRouter(
    tags=["some_tag"]
)


@router.get("/")
def get_some_obj():
    res = return_something()
    return res


# @router.get("", response_model=list[UserRead])
# async def get_users(
#     # session: AsyncSession = Depends(db_helper.session_getter),
#     session: Annotated[
#         AsyncSession,
#         Depends(db_helper.session_getter),
#     ],
# ):
#     users = await users_crud.get_all_users(session=session)
#     return users
