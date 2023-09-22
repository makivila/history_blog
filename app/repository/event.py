from ..models import Event, EventsAndPersonality


class EventRepository:
    def __init__(self, db_client) -> None:
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
        event = await self.collection_events.find_one({"_id": id})
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
    ):
        await self.collection_event_and_personality_ids.insert_one(
            events_and_personality.to_json()
        )
