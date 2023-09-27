from starlette import status
from starlette.requests import Request
from app.handler.helper.exceptions import ApplicationException, StatusType
from starlette.responses import JSONResponse
from app.dependencies import logger
import traceback
import uuid


def application_exception_handler(
    request: Request, exc: ApplicationException
) -> JSONResponse:
    if exc.status_type == StatusType.NOT_FOUND:
        status_code = status.HTTP_404_NOT_FOUND
    elif exc.status_type == StatusType.BAD_REQUEST:
        status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(exc.dict(), status_code=status_code)


def unexpected_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    error_id = uuid.uuid4()
    traceback_string = " ".join(traceback.format_tb(tb=exc.__traceback__))
    logger.error(
        f"Unexpected unhandled exception ({error_id}): {exc}",
        extra={
            "custom_dimensions": {"Error ID": error_id, "Traceback": traceback_string}
        },
    )
    return JSONResponse(
        f"Unexpected unhandled exception",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
