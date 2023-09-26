from ...models import Event
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.event import EventRepository
import traceback


class GetAllPersonalitiesUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, offset, limit) -> UsecaseResult:
        try:
            personalities = await self.repository.get_all_personalities(offset, limit)
            if not personalities:
                return UsecaseResult(
                    UsecaseStatus.BAD_REQUEST, "No personalities found"
                )
            return UsecaseResult(data=personalities)
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
