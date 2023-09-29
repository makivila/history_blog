from app.models import Personality, Career, EventsAndPersonality, Filters


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
        personality_dict = await self.collection_personality.find_one({"_id": id})
        if not personality_dict:
            return None
        personality = Personality(
            id=personality_dict["_id"],
            name=personality_dict["name"],
            career_id=personality_dict["career_id"],
            description=personality_dict["description"],
            interesting_facts=personality_dict["interesting_facts"],
            born=personality_dict["born"],
            died=personality_dict["died"],
            create_dt=personality_dict["create_dt"],
        )
        return personality

    async def get_personality_by_name(self, name: str):
        result = await self.collection_personality.find_one({"name": name})
        return result

    async def create_career(self, career: Career):
        new_career = await self.collection_career.insert_one(career.to_json())
        return new_career

    async def get_career_by_id(self, id: str):
        career_dict = await self.collection_career.find_one({"_id": id})
        if not career_dict:
            return None
        career = Career(name=career_dict["name"])
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

    async def get_all_personalities(self, filters: Filters):
        personalities_lst = []
        query = {
            "born": {
                "$gte": str(filters.start_date),
                "$lte": str(filters.end_date),
            }
        }
        cursor = (
            self.collection_personality.find(query)
            .sort(filters.sort_by, filters.direction)
            .skip(filters.offset)
            .limit(filters.limit)
        )

        for personality_dict in await cursor.to_list(length=filters.limit):
            personality = Personality(
                d=personality_dict["_id"],
                name=personality_dict["name"],
                career_id=personality_dict["career_id"],
                description=personality_dict["description"],
                interesting_facts=personality_dict["interesting_facts"],
                born=personality_dict["born"],
                died=personality_dict["died"],
                create_dt=personality_dict["create_dt"],
            )
            personalities_lst.append(personality)
        return personalities_lst

    async def get_all_careers(self, offset, limit):
        careers_lst = []
        cursor = self.collection_career.find().skip(offset).limit(limit)

        for career_dict in await cursor.to_list(length=limit):
            career = Career(id=career_dict["_id"], name=career_dict["name"])
            careers_lst.append(career)
        return careers_lst

    async def delete_personality_by_id(self, id) -> None:
        await self.collection_personality.delete_one({"_id": id})

    async def delete_career_by_id(self, id) -> None:
        await self.collection_career.delete_one({"_id": id})

    async def update_personality(self, personality: Personality) -> None:
        await self.collection_personality.replace_one(
            {"_id": personality.id}, personality.to_json()
        )

    async def update_career(self, career: Career) -> None:
        await self.collection_career.replace_one({"_id": career.id}, career.to_json())
