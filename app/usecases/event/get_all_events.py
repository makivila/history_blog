from app.handler.exceptions import NotPupsik
from ...models import Event
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.event import EventRepository
import traceback


class GetAllEventsUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, offset, limit) -> UsecaseResult:
        events = await self.repository.get_all_events(offset, limit)

        if not events:
            raise NotPupsik
            return UsecaseResult(UsecaseStatus.BAD_REQUEST, "No events found")
        return UsecaseResult(data=events)
