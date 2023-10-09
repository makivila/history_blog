from app.handler.helper.responses import success_response
from app.models import Event, EventPersonality, Filters
from app.dependencies import (
    create_usecase,
    add_personality_usecase,
    get_event_by_id_usecase,
    get_all_events_usecase,
    delete_event_by_id_usecase,
    update_event_usecase,
)
from fastapi import APIRouter
from fastapi import Depends
import datetime


event_router = APIRouter()


@event_router.post("/", response_description="Create new event", response_model=Event)
async def create_event(event: Event):
    event.create_dt = datetime.datetime.now()
    await create_usecase.execute(event)
    return success_response("Event successfully created")


@event_router.post(
    "/add_personality",
    response_description="Set personality by event",
    response_model=EventPersonality,
)
async def set_personality_by_event(event_personality: EventPersonality):
    await add_personality_usecase.execute(event_personality)
    return success_response("Personality set successfully")


@event_router.get("/{event_id}", response_description="Get event by id")
async def get_event_by_id(event_id: str):
    event = await get_event_by_id_usecase.execute(event_id)
    return success_response(event.to_json())


@event_router.get(
    "/",
    response_description="Get all events",
)
async def get_all_events(filter: Filters = Depends()):
    event_dicts = []
    event_models = await get_all_events_usecase.execute(filter)
    for event in event_models:
        event_dicts.append(event.to_json())
    return success_response(event_dicts)


@event_router.delete("/{event_id}", response_description="Delete event by id")
async def delete_event_by_id(event_id: str):
    await delete_event_by_id_usecase.execute(event_id)
    return success_response("Event successfully deleted")


@event_router.put(
    "/{event_id}", response_description="Update event", response_model=Event
)
async def update_event(event_id: str, event: Event):
    await update_event_usecase.execute(event_id, event)
    return success_response("Event successfully updated")
