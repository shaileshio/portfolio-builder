from .codes import ErrorCode


class AppError(Exception):
    """Base exception for application errors."""

    def __init__(
        self,
        detail: str,
        *,
        code: ErrorCode,
        status_code: int = 400,
    ) -> None:
        self.detail: str = detail
        self.code: ErrorCode = code
        self.status_code: int = status_code

        super().__init__(detail)


class UnauthorizedError(AppError):
    def __init__(
        self,
        message: str = "Authentication required",
        *,
        code: ErrorCode = ErrorCode.UNAUTHORIZED,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=401,
        )


class ForbiddenError(AppError):
    def __init__(
        self,
        message: str = "Access denied",
        *,
        code: ErrorCode = ErrorCode.FORBIDDEN,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=403,
        )


class NotFoundError(AppError):
    def __init__(
        self,
        message: str = "Resource not found",
        *,
        code: ErrorCode = ErrorCode.RESOURCE_NOT_FOUND,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=404,
        )
