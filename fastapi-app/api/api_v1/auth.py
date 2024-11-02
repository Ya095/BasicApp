from fastapi import APIRouter
from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.fastapi_users import fastapi_users
from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"]
)

# /login /logout
router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)
