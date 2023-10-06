from app.repository.career import CareerRepository
from app.models import Career


class UpdateCareerUsecase:
    def __init__(self, repository: CareerRepository) -> None:
        self.repository = repository

    async def execute(self, id: str, career: Career) -> None:
        career.id = id
        await self.repository.update_career(career)
