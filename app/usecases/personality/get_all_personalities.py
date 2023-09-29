from app.models import Personality, Filters
from app.repository.event import EventRepository
from typing import List


class GetAllPersonalitiesUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, filters: Filters) -> List[Personality]:
        personalities = await self.repository.get_all_personalities(filters)
        return personalities
