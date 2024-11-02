import uuid

from fastapi_users import FastAPIUsers

from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.user_manager import get_user_manager
from core.models import User


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [authentication_backend],
)