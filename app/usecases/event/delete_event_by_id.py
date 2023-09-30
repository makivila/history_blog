from app.handler.helper.exceptions import NotFoundException
from app.repository.event import EventRepository
from app.models import Event


class DeleteEventByIdUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> None:
        await self.repository.delete_event_by_id(id)
