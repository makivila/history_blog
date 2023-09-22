from ...models import Personality
from ...dto.usecase_result import UsecaseResult, UsecaseStatus
from ...repository.personality import PersonalityRepository
import traceback


class CreatePersonalityUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, personality: Personality) -> UsecaseResult:
        try:
            personality_exist = await self.repository.get_personality_by_name(
                personality.name
            )
            if personality_exist:
                return UsecaseResult(
                    UsecaseStatus.BAD_REQUEST, "This personality already exsist"
                )
            new_personality = await self.repository.create_personality(personality)
            result = await self.repository.get_personality_by_id(
                new_personality.inserted_id
            )
            if result:
                return UsecaseResult()
        except Exception as e:
            print(traceback.format_exc())
            return UsecaseResult(UsecaseStatus.INTERNAL_ERROR, e)
