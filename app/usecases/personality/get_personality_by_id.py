from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.event import EventRepository
import traceback


class GetPersonalityByIdUsecase:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> UsecaseResult:
        try:
            personality = await self.repository.get_personality_by_id(id)
            if not personality:
                return UsecaseResult(
                    UsecaseStatus.BAD_REQUEST, "This personality not found"
                )
            return UsecaseResult(data=personality)
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
