from fastapi import APIRouter

from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.fastapi_users import fastapi_users
from core.config import settings


router = APIRouter(
    prefix=settings.api_v1_prefix.auth,
    tags=["Auth"]
)

router.include_router(
    router=fastapi_users.get_users_router(authentication_backend),
)
