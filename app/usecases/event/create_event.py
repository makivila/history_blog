from app.handler.helper.exceptions import BadRequestException
from app.repository.event import EventRepository
from app.models import Event
import uuid


class CreateEventUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, event: Event) -> None:
        await self.repository.create_event(event)
