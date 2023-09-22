import datetime
from ..models import Personality, Career
from ..dependencies import create_usecase
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
    result = await create_usecase.execute(personality)
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
async def create_personality(career: Career):
    result = await create_usecase.execute(career)
    if result.status != UsecaseStatus.SUCCESS:
        return handle_failure_result(result)
    return success_response("Career successfully created")
