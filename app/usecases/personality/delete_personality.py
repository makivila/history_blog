from app.handler.helper.exceptions import NotFoundException
from app.repository.personality import PersonalityRepository


class DeletePersonalityByIdUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> None:
        personality = await self.repository.get_personality_by_id(id)
        if not personality:
            raise NotFoundException("This personality not found")
        await self.repository.delete_personality_by_id(id)
