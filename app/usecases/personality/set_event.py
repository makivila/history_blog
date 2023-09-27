from app.handler.helper.exceptions import BadRequestException
from app.repository.personality import PersonalityRepository
from app.models import EventsAndPersonality


class SetEventUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, events_and_personality: EventsAndPersonality) -> None:
        event = await self.repository.get_event_by_personality_id(
            events_and_personality.personality_id
        )
        if event["event_id"] == events_and_personality.event_id:
            raise BadRequestException(
                "This person is already associated with this event"
            )
        await self.repository.set_event_by_personality(events_and_personality)
