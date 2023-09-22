from ...models import EventsAndPersonality
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.personality import PersonalityRepository
import traceback


class SetPersonalityUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(
        self, events_and_personality: EventsAndPersonality
    ) -> UsecaseResult:
        try:
            personality = await self.repository.get_personality_by_event_id(
                events_and_personality.event_id
            )
            if personality["personality_id"] == events_and_personality.personality_id:
                return UsecaseResult(
                    UsecaseStatus.BAD_REQUEST,
                    "This event is already associated with this personality",
                )
            await self.repository.set_personality_by_event(events_and_personality)
            result = await self.repository.get_personality_by_event_id(
                events_and_personality.event_id
            )
            if result["personality_id"] == events_and_personality.personality_id:
                return UsecaseResult()
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
