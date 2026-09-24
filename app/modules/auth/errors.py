from app.core.exceptions import BadRequestError, ConflictError, NotFoundError


class ConfirmPasswordNotMatchError(BadRequestError):
    def __init__(
        self,
        detail: str = "Password it not meatch to confirm password",
        *,
        code: str = "confirm_password_not_match",
        status: int = 400,
    ) -> None:
        super().__init__(detail, code=code, status=status)


class UserNotFoundError(NotFoundError):
    def __init__(
        self,
        detail: str = "User not found",
        *,
        code: str = "user_not_found",
        status: int = 404,
    ) -> None:
        super().__init__(detail, code=code, status=status)


class EmailAlreadyExistError(ConflictError):
    def __init__(
        self,
        detail: str = "Email already exist",
        *,
        code: str = "email_exist",
        status: int = 409,
    ) -> None:
        super().__init__(detail, code=code, status=status)
