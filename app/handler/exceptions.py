from enum import Enum


class StatusType(Enum):
    INTERNAL_ERROR = 1
    NOT_FOUND = 2
    BAD_REQUEST = 3


class ApplicationException(Exception):
    def __init__(self, message, status_type) -> None:
        self.message = message
        self.status_type = status_type

    def dict(self):
        return {"message": self.message}


class NotPupsik(ApplicationException):
    def __init__(
        self, message="Pupsik not found", status_type=StatusType.NOT_FOUND
    ) -> None:
        super().__init__(message, status_type)
