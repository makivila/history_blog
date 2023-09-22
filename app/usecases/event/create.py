from ...models import Event
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.event import EventRepository


class CreateEventUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, event: Event) -> UsecaseResult:
        try:
            event_exist = await self.repository.get_event_by_name(event.name)
            if event_exist:
                return UsecaseResult(
                    UsecaseStatus.BAD_REQUEST, "This event already exsist"
                )
            new_event = await self.repository.create_event(event)
            result = await self.repository.get_event_by_id(new_event.inserted_id)
            if result:
                return UsecaseResult()
        except Exception as e:
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
