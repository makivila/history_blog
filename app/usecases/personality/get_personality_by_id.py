from app.handler.helper.exceptions import NotFoundException
from app.repository.event import EventRepository
from app.models import Personality


class GetPersonalityByIdUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> Personality:
        personality = await self.repository.get_personality_by_id(id)
        if not personality:
            raise NotFoundException("This personality not found")
        return personality
