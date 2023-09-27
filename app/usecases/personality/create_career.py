from ...repository.personality import PersonalityRepository
from app.handler.helper.exceptions import BadRequestException
from app.models import Career


class CreateCareerUsecase:
    def __init__(self, repository: PersonalityRepository) -> None:
        self.repository = repository

    async def execute(self, career: Career) -> None:
        career_exists = await self.repository.get_career_by_name(career.name)
        if career_exists:
            raise BadRequestException("This career already exsist")
        await self.repository.create_career(career)
