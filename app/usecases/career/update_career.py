from app.repository.personality import PersonalityRepository
from app.models import Career


class UpdateCareerUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, career: Career) -> None:
        career.id = id
        await self.repository.update_career(career)
