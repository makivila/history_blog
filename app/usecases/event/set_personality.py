from app.handler.helper.exceptions import BadRequestException
from app.repository.personality import PersonalityRepository
from app.models import EventsAndPersonality


class SetPersonalityUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, events_and_personality: EventsAndPersonality) -> None:
        personality = await self.repository.get_personality_by_event_id(
            events_and_personality.event_id
        )
        if personality["personality_id"] == events_and_personality.personality_id:
            raise BadRequestException(
                "This event is already associated with this personality"
            )
        await self.repository.set_personality_by_event(events_and_personality)
