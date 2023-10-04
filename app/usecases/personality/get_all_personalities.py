from app.repository.event import EventRepository
from app.models import Personality, Filters
from typing import List


class GetAllPersonalitiesUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, filters: Filters) -> List[Personality]:
        return await self.repository.get_all_personalities(filters)
