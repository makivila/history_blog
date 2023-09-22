class EventRepository:
    def __init__(self, db_client) -> None:
        self.db_client = db_client
        self.database = self.db_client.history_blog
        self.collection_events = self.database["events"]

    async def create_event(self, event):
        new_event = await self.collection_events.insert_one(event.to_json())
        return new_event

    async def get_event_by_id(self, id):
        event = await self.collection_events.find_one({"_id": id})
        return event

    async def get_event_by_name(self, name):
        result = await self.collection_events.find_one({"name": name})
        return result
