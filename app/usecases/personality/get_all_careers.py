from app.repository.event import EventRepository
from typing import List
from app.models import Career


class GetAllCareersUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, offset, limit) -> List[Career]:
        careers = await self.repository.get_all_careers(offset, limit)
        return careers
