from app.handler.helper.exceptions import NotFoundException
from app.repository.personality import PersonalityRepository
from app.models import Career


class UpdateCareerUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, career: Career) -> None:
        existing_career = await self.repository.get_career_by_id(id)
        if not existing_career:
            raise NotFoundException("This career not found")
        career.id = id
        await self.repository.update_career(career)
