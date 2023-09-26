import motor.motor_asyncio
from .config import Config

from .usecases.event.create import CreateEventUsecase
from .usecases.event.set_personality import SetPersonalityUsecase
from .usecases.event.get_event_by_id import GetEventByIdUsecase
from .usecases.event.get_all_events import GetAllEventsUsecase
from .usecases.event.delete_event_by_id import DeleteEventByIdUsecase

from .usecases.personality.create_personality import CreatePersonalityUsecase
from .usecases.personality.create_career import CreateCareerUsecase
from .usecases.personality.set_event import SetEventUsecase
from .usecases.personality.get_personality_by_id import GetPersonalityByIdUsecase
from .usecases.personality.get_all_personalities import GetAllPersonalitiesUsecase
from .usecases.personality.get_all_careers import GetAllCareersUsecase


from .repository.event import EventRepository
from .repository.personality import PersonalityRepository

client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGODB_URL)


event_repository = EventRepository(client)
personality_repository = PersonalityRepository(client)


create_usecase = CreateEventUsecase(event_repository)
set_personality_usecase = SetPersonalityUsecase(event_repository)
get_event_by_id_usecase = GetEventByIdUsecase(event_repository)
get_all_events_usecase = GetAllEventsUsecase(event_repository)
delete_event_by_id_usecase = DeleteEventByIdUsecase(event_repository)

create_personalit_usecase = CreatePersonalityUsecase(personality_repository)
create_career_usecase = CreateCareerUsecase(personality_repository)
set_event_usecase = SetEventUsecase(personality_repository)
get_personality_by_id_usecase = GetPersonalityByIdUsecase(personality_repository)
get_all_personalities_usecase = GetAllPersonalitiesUsecase(personality_repository)
get_all_careers_usecase = GetAllCareersUsecase(personality_repository)
