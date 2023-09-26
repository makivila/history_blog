import datetime
from ..models import Personality, Career, EventsAndPersonality
from ..dependencies import (
    create_personalit_usecase,
    create_career_usecase,
    set_event_usecase,
    get_personality_by_id_usecase,
    get_all_personalities_usecase,
    get_all_careers_usecase,
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
    "/personality/{personality_id}/", response_description="Get personality by id"
)
async def get_personality_by_id(personality_id: str):
    result = await get_personality_by_id_usecase.execute(personality_id)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response(result.data)


@personality_router.get("/personality", response_description="Get all personalities")
async def get_all_personalities(offset: int, limit: int):
    result = await get_all_personalities_usecase.execute(offset, limit)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response(result.data)


@personality_router.delete(
    "/personality/{personality_id}", response_description="Delete personality by id"
)
async def delete_personality_by_id(personality_id: str):
    result = await get_all_carers_usecase.execute(personality_id)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response(result.data)


@personality_router.get("/personality/career", response_description="Get all careers")
async def get_all_careers(offset: int, limit: int):
    result = await get_all_careers_usecase.execute(offset, limit)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response(result.data)


@personality_router.delete(
    "/personality/career/{career_id}", response_description="Delete career by id"
)
async def delete_career_by_id(career_id: str):
    result = await get_all_carers_usecase.execute(career_id)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response(result.data)
