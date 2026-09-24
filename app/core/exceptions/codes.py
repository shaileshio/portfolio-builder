from enum import StrEnum


class ErrorCode(StrEnum):
    FORBIDDEN = "forbidden"
    UNAUTHORIZED = "unauthorized"
    RESOURCE_NOT_FOUND = "resource_not_found"
    USER_NOT_FOUND = "user_not_found"
    INVALID_CREDENTIALS = "invalid_credentials"
    EMAIL_ALREADY_EXISTS = "email_already_exists"
