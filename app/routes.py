import datetime
from .models import Event
from .dependencies import database, get_value
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post("/event", response_description="Add new event", response_model=Event)
async def create_event(event: Event):
    event.create_dt = datetime.datetime.now()
    new_event = await database["events"].insert_one(event.to_json())
    created_event = await database["events"].find_one({"_id": new_event.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_event)
