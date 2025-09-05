from fastapi import status


class BaseException(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = "Internal Server Error"

    def __init__(
        self, status_code: int | None = None, message: str | None = None
    ) -> None:
        if status_code:
            self.status_code = status_code
        if message:
            self.message = message


class NotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Not Found"
