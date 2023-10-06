from app.handler.helper.exceptions import NotFoundException, AlreadyExistsException
from app.models import Career


class CareerRepository:
    def __init__(self, db_client) -> None:
        self.db_client = db_client
        self.database = self.db_client.history_blog
        self.collection_career = self.database["career"]

    async def create_career(self, career: Career):
        if await self.is_exists("name", career.name):
            raise AlreadyExistsException("This career already exsist")
        await self.collection_career.insert_one(career.to_json())

    async def is_exists(self, field, value):
        result = await self.collection_career.find_one({field: value})
        if result:
            return True
        else:
            return False

    async def delete_career_by_id(self, id) -> None:
        result = await self.collection_career.delete_one({"_id": id})
        if result.deleted_count == 0:
            raise NotFoundException("This career not found")

    async def get_all_careers(self, offset, limit):
        careers_lst = []
        cursor = self.collection_career.find().skip(offset).limit(limit)

        for career_dict in await cursor.to_list(length=limit):
            career = Career(id=career_dict["_id"], name=career_dict["name"])
            careers_lst.append(career)
        return careers_lst

    async def update_career(self, career: Career) -> None:
        if await self.is_exists("name", career.name):
            raise AlreadyExistsException("Career with this name already exists")
        result = await self.collection_career.replace_one(
            {"_id": career.id}, career.to_json()
        )
        if result.modified_count == 0:
            raise NotFoundException("This career not found")

    # async def get_career_by_id(self, id: str):
    #     career_dict = await self.collection_career.find_one({"_id": id})
    #     if not career_dict:
    #         raise NotFoundException
    #     career = Career(name=career_dict["name"])
    #     return career
