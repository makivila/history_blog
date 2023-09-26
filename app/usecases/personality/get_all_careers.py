from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.event import EventRepository
import traceback


class GetAllCareersUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, offset, limit) -> UsecaseResult:
        try:
            careers = await self.repository.get_all_careers(offset, limit)
            if not careers:
                return UsecaseResult(UsecaseStatus.BAD_REQUEST, "No careers found")
            return UsecaseResult(data=careers)
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
