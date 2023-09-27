from app.handler.helper.exceptions import NotFoundException
from app.repository.personality import PersonalityRepository
from app.models import Personality


class UpdatePersonalitytUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, personality: Personality) -> None:
        existing_personality = await self.repository.get_personality_by_id(id)
        if not existing_personality:
            raise NotFoundException("This personality not found")
        personality.id = id
        await self.repository.update_personality(personality)
