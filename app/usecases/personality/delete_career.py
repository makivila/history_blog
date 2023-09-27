from app.handler.helper.exceptions import NotFoundException
from app.repository.personality import PersonalityRepository


class DeleteCareerByIdUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> None:
        career = await self.repository.get_career_by_id(id)
        if not career:
            raise NotFoundException("This career not found")
        await self.repository.delete_career_by_id(id)
