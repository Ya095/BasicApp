from fastapi import APIRouter, Depends

from api.dependencies.authentication.fastapi_users import (
    current_active_user,
    current_active_superuser,
)
from core.config import settings
from core.models import User
from core.schemas.user import UserRead

# [Пример реализации]
# Скрытый контент, который доступен только определенному пользователю

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"]
)

@router.get("")
def get_user_messages(
    user: User = Depends(current_active_user)
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user)
    }

@router.get("/secrets")
def get_superuser_messages(
    user: User = Depends(current_active_superuser)
):
    return {
        "messages": ["secret-m1", "secret-m2", "secret-m3"],
        "user": UserRead.model_validate(user)
    }