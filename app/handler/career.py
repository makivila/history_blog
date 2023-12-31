from app.handler.helper.responses import success_response
from app.dependencies import (
    create_career_usecase,
    get_all_careers_usecase,
    delete_career_by_id_usecase,
    update_career_usecase,
)
from fastapi import APIRouter
from app.models import Career


career_router = APIRouter()


@career_router.post(
    "/",
    response_description="Create new career",
    response_model=Career,
)
async def create_career(career: Career):
    await create_career_usecase.execute(career)
    return success_response("Career successfully created")


@career_router.get("/", response_description="Get all careers")
async def get_all_careers(offset: int, limit: int):
    career_model = await get_all_careers_usecase.execute(offset, limit)
    career_dicts = []
    for career in career_model:
        career_dicts.append(career.to_json())
    return success_response(career_dicts)


@career_router.delete("/{career_id}", response_description="Delete career by id")
async def delete_career_by_id(career_id: str):
    await delete_career_by_id_usecase.execute(career_id)
    return success_response("Career successfully deleted")


@career_router.put(
    "/{career_id}",
    response_description="Update career",
    response_model=Career,
)
async def update_career(career_id: str, career: Career):
    await update_career_usecase.execute(career_id, career)
    return success_response("Career successfully updated")
