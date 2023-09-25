import motor.motor_asyncio
from .config import Config

from .usecases.event.create import CreateEventUsecase
from .usecases.event.set_personality import SetPersonalityUsecase
from .usecases.event.get_event_by_id import GetEventByIdUsecase

from .usecases.personality.create_personality import CreatePersonalityUsecase
from .usecases.personality.create_career import CreateCareerUsecase
from .usecases.personality.set_event import SetEventUsecase
from .usecases.personality.get_personality_by_id import GetPersonalityByIdUsecase


from .repository.event import EventRepository
from .repository.personality import PersonalityRepository

client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGODB_URL)


event_repository = EventRepository(client)
personality_repository = PersonalityRepository(client)


create_usecase = CreateEventUsecase(event_repository)
set_personality_usecase = SetPersonalityUsecase(event_repository)
get_event_by_id_usecase = GetEventByIdUsecase(event_repository)

create_personalit_usecase = CreatePersonalityUsecase(personality_repository)
create_career_usecase = CreateCareerUsecase(personality_repository)
set_event_usecase = SetEventUsecase(personality_repository)
get_personality_by_id_usecase = GetPersonalityByIdUsecase(personality_repository)
# database = client.fastapi_project
# collection = database.events
# database = client["fastapi_project"]
# async def get_value(database):
#     collection = await database["events"].find().to_list(length=100)
