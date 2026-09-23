class AppError(Exception):
    def __init__(self, deatil: object) -> None:
        self.detail: object = deatil


class HttpError(AppError):
    def __init__(self, deatil: object, status_code: int) -> None:
        self.status_code: int = status_code

        super().__init__(deatil)
