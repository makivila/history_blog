from app.repository.personality import PersonalityRepository


class DeletePersonalityByIdUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> None:
        await self.repository.delete_personality_by_id(id)
