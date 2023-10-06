from app.repository.career import CareerRepository
from typing import List
from app.models import Career


class GetAllCareersUsecase:
    def __init__(self, repository: CareerRepository) -> None:
        self.repository = repository

    async def execute(self, offset, limit) -> List[Career]:
        return await self.repository.get_all_careers(offset, limit)
