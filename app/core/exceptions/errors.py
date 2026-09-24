class AppError(Exception):
    def __init__(self, detail: str) -> None:
        self.detail = detail

        super().__init__(detail)


class HttpError(AppError):
    def __init__(self, detail: str, *, code: str, status: int) -> None:
        self.code = code
        self.status = status

        super().__init__(detail)


class UnauthorizedError(HttpError):
    def __init__(
        self,
        detail: str = "Authentication required",
        *,
        code: str = "unauthorized",
        status: int = 401,
    ) -> None:
        super().__init__(detail, code=code, status=status)


class ForbiddenError(HttpError):
    def __init__(
        self,
        detail: str = "Access denied",
        *,
        code: str = "forbidden",
        status: int = 403,
    ) -> None:
        super().__init__(detail, code=code, status=status)


class NotFoundError(HttpError):
    def __init__(
        self,
        detail: str = "Resource not found",
        *,
        code: str = "not_found",
        status: int = 404,
    ) -> None:
        super().__init__(detail, code=code, status=status)


class ConflictError(HttpError):
    def __init__(
        self,
        detail: str = "Resource conflict",
        *,
        code: str = "conflict",
        status: int = 409,
    ) -> None:
        super().__init__(detail, code=code, status=status)


class BadRequestError(HttpError):
    def __init__(
        self,
        detail: str = "Bad request",
        *,
        code: str = "bad_request",
        status: int = 400,
    ) -> None:
        super().__init__(detail, code=code, status=status)
