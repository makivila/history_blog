from starlette import status
from starlette.requests import Request
from .exceptions import ApplicationException, StatusType
from starlette.responses import JSONResponse


def application_exception_handler(
    request: Request, exc: ApplicationException
) -> JSONResponse:
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    if exc.status_type == StatusType.NOT_FOUND:
        status_code = status.HTTP_404_NOT_FOUND
    elif exc.status_type == StatusType.BAD_REQUEST:
        status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(exc.dict(), status_code=status_code)


def unexpected_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse("Hello", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
