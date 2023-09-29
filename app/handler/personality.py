from app.models import Personality, Career, EventsAndPersonality, Filters
from app.handler.helper.responses import success_response
from app.dependencies import (
    create_personalit_usecase,
    create_career_usecase,
    set_event_usecase,
    get_personality_by_id_usecase,
    get_all_personalities_usecase,
    get_all_careers_usecase,
    delete_career_by_id_usecase,
    delete_personality_by_id_usecase,
    update_personalityt_usecase,
    update_career_usecase,
)
from fastapi import APIRouter
from fastapi import Depends
import datetime


personality_router = APIRouter()


@personality_router.post(
    "/personality",
    response_description="Create new personality",
    response_model=Personality,
)
async def create_personality(personality: Personality):
    personality.create_dt = datetime.datetime.now()
    await create_personalit_usecase.execute(personality)
    return success_response("Personality successfully created")


@personality_router.post(
    "/personality/career",
    response_description="Create new career",
    response_model=Career,
)
async def create_career(career: Career):
    await create_career_usecase.execute(career)
    return success_response("Career successfully created")


@personality_router.post(
    "/personality/set_event",
    response_description="Set event by personality",
    response_model=EventsAndPersonality,
)
async def set_event_by_personality(events_and_personality: EventsAndPersonality):
    await set_event_usecase.execute(events_and_personality)
    return success_response("Event set successfully")


@personality_router.get(
    "/personality/{personality_id}/", response_description="Get personality by id"
)
async def get_personality_by_id(personality_id: str):
    result = await get_personality_by_id_usecase.execute(personality_id)
    return success_response(result.to_json())


@personality_router.get("/personality", response_description="Get all personalities")
async def get_all_personalities(filter: Filters = Depends()):
    personality_dicts = []
    personalities_model = await get_all_personalities_usecase.execute(filter)
    for personality in personalities_model:
        personality_dicts.append(personality.to_json())
    return success_response(personality_dicts)


@personality_router.delete(
    "/personality/{personality_id}", response_description="Delete personality by id"
)
async def delete_personality_by_id(personality_id: str):
    await delete_personality_by_id_usecase.execute(personality_id)
    return success_response("Personality successfully deleted")


@personality_router.get("/personality/career", response_description="Get all careers")
async def get_all_careers(offset: int, limit: int):
    result = await get_all_careers_usecase.execute(offset, limit)
    return success_response(result.data)


@personality_router.delete(
    "/personality/career/{career_id}", response_description="Delete career by id"
)
async def delete_career_by_id(career_id: str):
    await delete_career_by_id_usecase.execute(career_id)
    return success_response("Career successfully deleted")


@personality_router.put(
    "/personality/{personality_id}",
    response_description="Update personality",
    response_model=Personality,
)
async def update_personality(personality_id: str, personality: Personality):
    await update_personalityt_usecase.execute(personality_id, personality)
    return success_response("Personality successfully updated")


@personality_router.put(
    "/personality/career/{career_id}",
    response_description="Update career",
    response_model=Career,
)
async def update_career(career_id: str, career: Career):
    await update_career_usecase.execute(career_id, career)
    return success_response("Career successfully updated")
