from app.repository.personality import PersonalityRepository
from app.models import Personality


class UpdatePersonalitytUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, personality: Personality) -> None:
        old_personality = await self.repository.get_personality_by_id(id)
        personality.id = id
        personality.create_id = old_personality.create_id
        await self.repository.update_personality(personality)
