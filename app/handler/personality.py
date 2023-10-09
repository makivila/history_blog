from app.models import Personality, EventPersonality, Filters
from app.handler.helper.responses import success_response
from app.dependencies import (
    create_personalit_usecase,
    add_event_usecase,
    get_personality_by_id_usecase,
    get_all_personalities_usecase,
    delete_personality_by_id_usecase,
    update_personalityt_usecase,
)
from fastapi import APIRouter
from fastapi import Depends
import datetime


personality_router = APIRouter()


@personality_router.post(
    "/",
    response_description="Create new personality",
    response_model=Personality,
)
async def create_personality(personality: Personality):
    personality.create_dt = datetime.datetime.now()
    await create_personalit_usecase.execute(personality)
    return success_response("Personality successfully created")


@personality_router.post(
    "/add_event",
    response_description="Set event by personality",
    response_model=EventPersonality,
)
async def set_event_by_personality(event_personality: EventPersonality):
    await add_event_usecase.execute(event_personality)
    return success_response("Event set successfully")


@personality_router.get(
    "/{personality_id}/", response_description="Get personality by id"
)
async def get_personality_by_id(personality_id: str):
    result = await get_personality_by_id_usecase.execute(personality_id)
    return success_response(result.to_json())


@personality_router.get("/", response_description="Get all personalities")
async def get_all_personalities(filter: Filters = Depends()):
    personality_dicts = []
    personalities_model = await get_all_personalities_usecase.execute(filter)
    for personality in personalities_model:
        personality_dicts.append(personality.to_json())
    return success_response(personality_dicts)


@personality_router.delete(
    "/{personality_id}", response_description="Delete personality by id"
)
async def delete_personality_by_id(personality_id: str):
    await delete_personality_by_id_usecase.execute(personality_id)
    return success_response("Personality successfully deleted")


@personality_router.put(
    "/{personality_id}",
    response_description="Update personality",
    response_model=Personality,
)
async def update_personality(personality_id: str, personality: Personality):
    await update_personalityt_usecase.execute(personality_id, personality)
    return success_response("Personality successfully updated")
