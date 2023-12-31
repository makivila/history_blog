from enum import Enum


class StatusType(Enum):
    INTERNAL_ERROR = 1
    NOT_FOUND = 2
    BAD_REQUEST = 3
    ALREADY_EXISTS = 4


class ApplicationException(Exception):
    def __init__(self, message, status_type) -> None:
        self.message = message
        self.status_type = status_type

    def dict(self):
        return {"message": self.message}


class NotFoundException(ApplicationException):
    def __init__(self, message="Not found", status_type=StatusType.NOT_FOUND) -> None:
        super().__init__(message, status_type)


class BadRequestException(ApplicationException):
    def __init__(
        self, message="Bad request", status_type=StatusType.BAD_REQUEST
    ) -> None:
        super().__init__(message, status_type)


class AlreadyExistsException(ApplicationException):
    def __init__(
        self, message="Bad request", status_type=StatusType.ALREADY_EXISTS
    ) -> None:
        super().__init__(message, status_type)
