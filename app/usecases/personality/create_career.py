from ...models import Career
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.personality import PersonalityRepository
import traceback


class CreateCareerUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, career: Career) -> UsecaseResult:
        try:
            career_exists = await self.repository.get_career_by_name(career.name)
            if career_exists:
                return UsecaseResult(
                    UsecaseStatus.BAD_REQUEST, "This career already exsist"
                )
            new_career = await self.repository.create_career(career)
            result = await self.repository.get_career_by_id(new_career.inserted_id)
            if result:
                return UsecaseResult()
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
