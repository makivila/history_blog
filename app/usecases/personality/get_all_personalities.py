from app.models import Event
from app.repository.event import EventRepository
from typing import List


class GetAllPersonalitiesUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, offset, limit) -> List[Event]:
        personalities = await self.repository.get_all_personalities(offset, limit)
        return personalities
