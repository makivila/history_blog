from app.handler.helper.exceptions import BadRequestException
from app.repository.personality import PersonalityRepository
from app.models import EventPersonality


class AddPersonalityUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, event_personality: EventPersonality) -> None:
        await self.repository.set_personality_by_event(event_personality)
