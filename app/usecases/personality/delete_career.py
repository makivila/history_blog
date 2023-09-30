from app.repository.personality import PersonalityRepository


class DeleteCareerByIdUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> None:
        await self.repository.delete_career_by_id(id)
