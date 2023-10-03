from starlette.responses import JSONResponse
from fastapi import status
from typing import Any
import json


def success_response(data: Any = None) -> JSONResponse:
    if data is not None:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": "success", "data": data},
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"status : success"}
        )
