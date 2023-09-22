from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ..helper.responses import failure_response
from fastapi.responses import JSONResponse
from fastapi import status


def handle_failure_result(result: UsecaseResult) -> JSONResponse:
    if result.status == UsecaseStatus.INTERNAL_ERROR:
        return failure_response(
            f"internal error: {result.data}", status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    elif result.status == UsecaseStatus.BAD_REQUEST:
        return failure_response(
            f"bad request: {result.data}", status.HTTP_400_BAD_REQUEST
        )
    elif result.status == UsecaseStatus.NOT_FOUND:
        return failure_response(
            f"resource not found: {result.data}", status.HTTP_404_NOT_FOUND
        )
    else:
        return failure_response("unknown error", status.HTTP_500_INTERNAL_SERVER_ERROR)
