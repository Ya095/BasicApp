from fastapi import APIRouter
from core.config import settings
from .some_api import router as some_router


# Подключение роутера(ов)
router = APIRouter(
    prefix=settings.api_v1_prefix
)

router.include_router(some_router)
