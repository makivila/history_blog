from app.repository.personality import PersonalityRepository
from app.models import Personality


class UpdatePersonalitytUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, personality: Personality) -> None:
        personality.id = id
        await self.repository.update_personality(personality)
