class AppError(Exception):
    """Base exception for application errors."""

    def __init__(self, detail: str, *, code: str, status_code: int = 400) -> None:
        self.detail: str = detail
        self.code: str = code
        self.status_code: int = status_code

        super().__init__(detail)


class UnauthorizedError(AppError):
    detail: str = "Authentication required"
    code: str = "unauthorized"
    status_code = 401


class ForbiddenError(AppError):
    detail: str = "Access denied"
    code: str = "forbidden"
    status_code = 403


class NotFoundError(AppError):
    detail: str = "Resource not found"
    code: str = "not_found"
    status_code = 404


class ConflictError(AppError):
    detail: str = "Resource conflict"
    code: str = "conflict"
    status_code = 409


class BadRequestError(AppError):
    detail: str = "Bad request"
    code: str = "bad_request"
    status_code = 400
