from ...models import Event
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.event import EventRepository
import traceback


class GetEventByIdUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> UsecaseResult:
        try:
            event = await self.repository.get_event_by_id(id)
            if not event:
                return UsecaseResult(UsecaseStatus.BAD_REQUEST, "This event not found")
            return UsecaseResult(data=event)
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)