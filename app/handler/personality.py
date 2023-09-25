import datetime
from ..models import Personality, Career, EventsAndPersonality
from ..dependencies import (
    create_personalit_usecase,
    create_career_usecase,
    set_event_usecase,
    get_personality_by_id_usecase,
)
from fastapi import APIRouter, status
from .helper.responses import failure_response, success_response
from .helper.handle_failure_result import handle_failure_result
from ..dto.usecase_result import UsecaseResult, UsecaseStatus


personality_router = APIRouter()


@personality_router.post(
    "/personality",
    response_description="Create new personality",
    response_model=Personality,
)
async def create_personality(personality: Personality):
    personality = await add_creation_time(personality)
    result = await create_personalit_usecase.execute(personality)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response("Personality successfully created")


async def add_creation_time(personality):
    personality.create_dt = datetime.datetime.now()
    return personality


@personality_router.post(
    "/personality/career",
    response_description="Create new career",
    response_model=Career,
)
async def create_career(career: Career):
    result = await create_career_usecase.execute(career)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response("Career successfully created")


@personality_router.post(
    "/personality/set_event",
    response_description="Set event by personality",
    response_model=EventsAndPersonality,
)
async def set_event_by_personality(events_and_personality: EventsAndPersonality):
    result = await set_event_usecase.execute(events_and_personality)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response("Event set successfully")


@personality_router.get(
    "/personality/{personality_id}/",
    response_description="Get personality by id",
    response_model=EventsAndPersonality,
)
async def get_personality_by_id(personality_id: str):
    result = await get_personality_by_id_usecase.execute(personality_id)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response(result.data)
