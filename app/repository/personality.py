from ..models import Personality, Career


class PersonalityRepository:
    def __init__(self, db_client) -> None:
        self.db_client = db_client
        self.database = self.db_client.history_blog
        self.collection_personality = self.database["personality"]
        self.collection_career = self.database["career"]

    async def create_personality(self, personality: Personality):
        new_personality = await self.collection_personality.insert_one(
            personality.to_json()
        )
        return new_personality

    async def get_event_by_id(self, id: str):
        personality = await self.collection_personality.find_one({"_id": id})
        return personality

    async def get_event_by_name(self, name: str):
        result = await self.collection_personality.find({"name": name})
        return result

    async def create_career(self, career: Career):
        new_career = await self.collection_career.insert_one(career.to_json())
        return new_career

    async def get_career_by_id(self, id: str):
        career = await self.collection_career.find_one({"_id": id})
        return career

    async def get_career_by_name(self, name: str):
        result = await self.collection_career.find({"name": name})
        return result
