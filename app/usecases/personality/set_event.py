from ...models import EventsAndPersonality
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.personality import PersonalityRepository
import traceback


class SetEventUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(
        self, events_and_personality: EventsAndPersonality
    ) -> UsecaseResult:
        try:
            event = await self.repository.get_event_by_personality_id(
                events_and_personality.personality_id
            )
            if event["event_id"] == events_and_personality.event_id:
                return UsecaseResult(
                    UsecaseStatus.BAD_REQUEST,
                    "This person is already associated with this event",
                )
            await self.repository.set_event_by_personality(events_and_personality)
            result = await self.repository.get_event_by_personality_id(
                events_and_personality.personality_id
            )
            if result["event_id"] == events_and_personality.event_id:
                return UsecaseResult()
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
