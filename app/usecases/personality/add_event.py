from app.repository.personality import PersonalityRepository
from app.models import EventPersonality


class AddEventUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, event_personality: EventPersonality) -> None:
        await self.repository.set_event_by_personality(event_personality)
