from app.models import Personality
from app.repository.personality import PersonalityRepository
from app.handler.helper.exceptions import BadRequestException


class CreatePersonalityUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, personality: Personality) -> None:
        personality_exist = await self.repository.get_personality_by_name(
            personality.name
        )
        if personality_exist:
            raise BadRequestException("This personality already exsist")
        await self.repository.create_personality(personality)
