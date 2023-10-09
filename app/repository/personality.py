from app.handler.helper.exceptions import NotFoundException, AlreadyExistsException
from app.models import Personality, EventPersonality, Filters


class PersonalityRepository:
    def __init__(self, db_client) -> None:
        self.collection_personality = db_client.db_client.history_blog.database[
            "personality"
        ]
        self.collection_event_personality_ids = (
            db_client.db_client.history_blog.database["event_personality_ids"]
        )

    async def create_personality(self, personality: Personality):
        if await self.is_exists("name", personality.name):
            raise AlreadyExistsException("This personality already exsist")
        await self.collection_personality.insert_one(personality.to_json())

    async def is_exists(self, field, value):
        result = await self.collection_personality.find_one({field: value})
        if result:
            return True
        else:
            return False

    async def delete_personality_by_id(self, id) -> None:
        result = await self.collection_personality.delete_one({"_id": id})
        await self.collection_event_and_personality_ids.delete_many(
            {"personality_id": id}
        )
        if result.deleted_count == 0:
            raise NotFoundException("This personality not found")

    async def get_personality_by_id(self, id: str):
        personality_dict = await self.collection_personality.find_one({"_id": id})
        if not personality_dict:
            raise NotFoundException
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

    async def update_personality(self, personality: Personality) -> None:
        if await self.is_exists("name", personality.name):
            raise AlreadyExistsException("Personality with this name already exists")
        result = await self.collection_personality.replace_one(
            {"_id": personality.id}, personality.to_json()
        )
        if result.matched_count == 0:
            raise NotFoundException("This personality not found")

    async def set_event_by_personality(self, event_personality: EventPersonality):
        if await self.is_exists_event_by_personality(event_personality):
            raise AlreadyExistsException(
                "This person is already associated with this event"
            )
        await self.collection_event_personality_ids.insert_one(
            event_personality.to_json()
        )

    async def is_exists_event_by_personality(self, event_personality: EventPersonality):
        result = await self.collection_event_personality_ids.find_one(
            {"personality_id": event_personality.personality_id}
        )
        if result:
            if result["event_id"] == event_personality.event_id:
                return True
            else:
                return False
        return False
