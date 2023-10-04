from app.repository.personality import PersonalityRepository
from app.models import Personality


class CreatePersonalityUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, personality: Personality) -> None:
        await self.repository.create_personality(personality)
