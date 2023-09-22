import datetime
from ..models import Event
from ..dependencies import create_usecase
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .helper.responses import failure_response, success_response
from .helper.handle_failure_result import handle_failure_result
from ..dto.usecase_result import UsecaseResult, UsecaseStatus


event_router = APIRouter()


@event_router.post(
    "/event", response_description="Create new event", response_model=Event
)
async def create_event(event: Event):
    event = await add_creation_time(event)
    result = await create_usecase.execute(event)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response("Event successfully created")


async def add_creation_time(event):
    event.create_dt = datetime.datetime.now()
    return event
