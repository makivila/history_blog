import datetime
from ..models import Event, EventsAndPersonality
from ..dependencies import create_usecase, set_personality_usecase
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


@event_router.post(
    "/event/set_personality",
    response_description="Set personality by event",
    response_model=EventsAndPersonality,
)
async def set_personality_by_event(events_and_personality: EventsAndPersonality):
    result = await set_personality_usecase.execute(events_and_personality)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response("Personality set successfully")


@event_router.get(
    "/event/{event_id}/",
    response_description="Get event by id",
    response_model=EventsAndPersonality,
)
async def get_event_by_id(event_id: str):
    result = await se_personality_usecase.execute(event_id)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response()
