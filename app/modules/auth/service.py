from app.core.security.hashing import get_hasher
from app.db.models.user import User
from app.db.repositories import UserRepository

from .errors import ConfirmPasswordNotMatchError, EmailAlreadyExistError
from .schemas import RegisterRequest


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_active_user(self, data: RegisterRequest) -> User:
        if data.password != data.confirm_password:
            raise ConfirmPasswordNotMatchError

        hasher = get_hasher()
        password_hash = hasher.hash(data.password)

        if await self.repository.email_exists(data.email):
            raise EmailAlreadyExistError

        return await self.repository.create(data.email, password_hash)
