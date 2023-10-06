from app.repository.career import CareerRepository


class DeleteCareerByIdUsecase:
    def __init__(self, repository: CareerRepository) -> None:
        self.repository = repository

    async def execute(self, id: str) -> None:
        await self.repository.delete_career_by_id(id)
