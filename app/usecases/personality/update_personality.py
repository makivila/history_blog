from app.repository.personality import PersonalityRepository
from app.models import Personality


class UpdatePersonalitytUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, personality: Personality) -> None:
        old_personality = await self.repository.get_personality_by_id(id)
        personality.id = id
        personality.create_dt = old_personality.create_dt
        await self.repository.update_personality(personality)
