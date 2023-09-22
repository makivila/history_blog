import motor.motor_asyncio
from .config import Config

from .usecases.event.create import CreateEventUsecase
from .usecases.personality.create_personality import CreatePersonalityUsecase


from .repository.event import EventRepository
from .repository.personality import PersonalityRepository

client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGODB_URL)


event_repository = EventRepository(client)
personality_repository = PersonalityRepository(client)


create_usecase = CreateEventUsecase(event_repository)
create_personalit_usecase = CreatePersonalityUsecase(personality_repository)


# database = client.fastapi_project
# collection = database.events
# database = client["fastapi_project"]
# async def get_value(database):
#     collection = await database["events"].find().to_list(length=100)
