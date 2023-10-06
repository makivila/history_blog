from app.repository.career import CareerRepository

from app.models import Career


class CreateCareerUsecase:
    def __init__(self, repository: CareerRepository) -> None:
        self.repository = repository

    async def execute(self, career: Career) -> None:
        await self.repository.create_career(career)
