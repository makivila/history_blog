from app.repository.event import EventRepository
from app.models import Event, Filters
from typing import List


class GetAllEventsUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, filters: Filters) -> List[Event]:
        return await self.repository.get_all_events(filters)
