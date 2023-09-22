from fastapi.responses import JSONResponse
from fastapi import status
from typing import Any
import json


def success_response(message: Any = None) -> JSONResponse:
    if message:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=f"status: success, message: {message}",
        )
    else:
        return JSONResponse(status_code=status.HTTP_200_OK, content="status : success")


def failure_response(message: Any, status_code: int) -> JSONResponse:
    return JSONResponse(
        status_code=status_code, content=f"status: failure, message: {message}"
    )
