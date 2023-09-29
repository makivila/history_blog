from app.models import Event, EventsAndPersonality, Filters
import motor.motor_asyncio
from typing import List


class EventRepository:
    def __init__(self, db_client: motor.motor_asyncio.AsyncIOMotorClient) -> None:
        self.db_client = db_client
        self.database = self.db_client.history_blog
        self.collection_events = self.database["events"]
        self.collection_event_and_personality_ids = self.database[
            "event_and_personality_ids"
        ]

    async def create_event(self, event: Event):
        new_event = await self.collection_events.insert_one(event.to_json())
        return new_event

    async def get_event_by_id(self, id):
        event_dict = await self.collection_events.find_one({"_id": id})
        if not event_dict:
            return None
        event = Event(
            id=event_dict["_id"],
            name=event_dict["name"],
            start_date=event_dict["start_date"],
            end_date=event_dict["end_date"],
            create_dt=event_dict["create_dt"],
            description=event_dict["description"],
            victim_numbers=event_dict["victim_numbers"],
            interesting_facts=event_dict["interesting_facts"],
        )
        return event

    async def get_event_by_name(self, name):
        result = await self.collection_events.find_one({"name": name})
        return result

    async def get_personality_by_event_id(self, event_id):
        result = await self.collection_event_and_personality_ids.find_one(
            {"event_id": event_id}
        )
        return result

    async def set_personality_by_event(
        self, events_and_personality: EventsAndPersonality
    ) -> None:
        await self.collection_event_and_personality_ids.insert_one(
            events_and_personality.to_json()
        )

    async def get_all_events(self, filters: Filters) -> List[Event]:
        events_lst = []

        query = {
            "start_date": {
                "$gte": str(filters.start_date),
                "$lte": str(filters.end_date),
            }
        }
        cursor = (
            self.collection_events.find(query)
            .sort(filters.sort_by, filters.direction)
            .skip(filters.offset)
            .limit(filters.limit)
        )

        for event_dict in await cursor.to_list(length=filters.limit):
            event = Event(
                id=event_dict["_id"],
                name=event_dict["name"],
                start_date=event_dict["start_date"],
                end_date=event_dict["end_date"],
                create_dt=event_dict["create_dt"],
                description=event_dict["description"],
                victim_numbers=event_dict["victim_numbers"],
                interesting_facts=event_dict["interesting_facts"],
            )
            events_lst.append(event)
        return events_lst

    async def delete_event_by_id(self, id) -> None:
        await self.collection_events.delete_one({"_id": id})

    async def update_event(self, event: Event) -> None:
        await self.collection_events.replace_one({"_id": event.id}, event.to_json())
