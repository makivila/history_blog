from ..models import Personality, Career, EventsAndPersonality


class PersonalityRepository:
    def __init__(self, db_client) -> None:
        self.db_client = db_client
        self.database = self.db_client.history_blog
        self.collection_personality = self.database["personality"]
        self.collection_career = self.database["career"]
        self.collection_event_and_personality_ids = self.database[
            "event_and_personality_ids"
        ]

    async def create_personality(self, personality: Personality):
        new_personality = await self.collection_personality.insert_one(
            personality.to_json()
        )
        return new_personality

    async def get_personality_by_id(self, id: str):
        personality = await self.collection_personality.find_one({"_id": id})
        return personality

    async def get_personality_by_name(self, name: str):
        result = await self.collection_personality.find_one({"name": name})
        return result

    async def create_career(self, career: Career):
        new_career = await self.collection_career.insert_one(career.to_json())
        return new_career

    async def get_career_by_id(self, id: str):
        career = await self.collection_career.find_one({"_id": id})
        return career

    async def get_career_by_name(self, name: str):
        result = await self.collection_career.find_one({"name": name})
        return result

    async def get_event_by_personality_id(self, personality_id):
        result = await self.collection_event_and_personality_ids.find_one(
            {"personality_id": personality_id}
        )
        return result

    async def set_event_by_personality(
        self, events_and_personality: EventsAndPersonality
    ):
        await self.collection_event_and_personality_ids.insert_one(
            events_and_personality.to_json()
        )

    async def get_all_personalities(self, offset, limit):
        personalities_lst = []
        cursor = self.collection_personality.find().skip(offset).limit(limit)

        for personality in await cursor.to_list(length=limit):
            personalities_lst.append(personality)
        return personalities_lst

    async def get_all_careers(self, offset, limit):
        careers_lst = []
        cursor = self.collection_career.find().skip(offset).limit(limit)

        for career in await cursor.to_list(length=limit):
            careers_lst.append(career)
        return careers_lst
