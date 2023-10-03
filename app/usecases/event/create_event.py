from app.handler.helper.exceptions import BadRequestException
from app.repository.event import EventRepository
from app.models import Event
import uuid


class CreateEventUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, event: Event) -> None:
        # event.id = str(uuid.uuid4())
        # existing_event = await self.repository.get_event_by_name(event.name)
        # if existing_event:
        #     raise BadRequestException("This event already exists")
        await self.repository.create_event(event)
