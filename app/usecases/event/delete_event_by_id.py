from app.handler.helper.exceptions import NotFoundException
from app.repository.event import EventRepository
from app.models import Event


class DeleteEventByIdUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> None:
        event = await self.repository.get_event_by_id(id)
        if not event:
            raise NotFoundException("This event not found")
        await self.repository.delete_event_by_id(id)
