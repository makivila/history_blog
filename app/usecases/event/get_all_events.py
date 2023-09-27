from app.repository.event import EventRepository
from app.models import Event
from typing import List


class GetAllEventsUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, offset: int, limit: int) -> List[Event]:
        events = await self.repository.get_all_events(offset, limit)
        return events
