import motor.motor_asyncio
from app.config import Config
from app.logger import create_logger

from app.usecases.event.create_event import CreateEventUsecase
from app.usecases.event.set_personality import SetPersonalityUsecase
from app.usecases.event.get_event_by_id import GetEventByIdUsecase
from app.usecases.event.get_all_events import GetAllEventsUsecase
from app.usecases.event.delete_event_by_id import DeleteEventByIdUsecase
from app.usecases.event.update_event import UpdateEventUsecase

from app.usecases.personality.create_personality import CreatePersonalityUsecase
from app.usecases.personality.set_event import SetEventUsecase
from app.usecases.personality.get_personality_by_id import GetPersonalityByIdUsecase
from app.usecases.personality.get_all_personalities import GetAllPersonalitiesUsecase
from app.usecases.personality.delete_personality import DeletePersonalityByIdUsecase
from app.usecases.personality.update_personality import UpdatePersonalitytUsecase

from app.usecases.career.update_career import UpdateCareerUsecase
from app.usecases.career.get_all_careers import GetAllCareersUsecase
from app.usecases.career.delete_career import DeleteCareerByIdUsecase
from app.usecases.career.create_career import CreateCareerUsecase

from app.repository.event import EventRepository
from app.repository.personality import PersonalityRepository
from app.repository.career import CareerRepository

logger = create_logger()
client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGODB_URL)


event_repository = EventRepository(client)
personality_repository = PersonalityRepository(client)
career_repository = CareerRepository(client)


create_usecase = CreateEventUsecase(event_repository)
set_personality_usecase = SetPersonalityUsecase(event_repository)
get_event_by_id_usecase = GetEventByIdUsecase(event_repository)
get_all_events_usecase = GetAllEventsUsecase(event_repository)
delete_event_by_id_usecase = DeleteEventByIdUsecase(event_repository)
update_event_usecase = UpdateEventUsecase(event_repository)

create_personalit_usecase = CreatePersonalityUsecase(personality_repository)
set_event_usecase = SetEventUsecase(personality_repository)
get_personality_by_id_usecase = GetPersonalityByIdUsecase(personality_repository)
get_all_personalities_usecase = GetAllPersonalitiesUsecase(personality_repository)
delete_personality_by_id_usecase = DeletePersonalityByIdUsecase(personality_repository)
update_personalityt_usecase = UpdatePersonalitytUsecase(personality_repository)

update_career_usecase = UpdateCareerUsecase(career_repository)
delete_career_by_id_usecase = DeleteCareerByIdUsecase(career_repository)
create_career_usecase = CreateCareerUsecase(career_repository)
get_all_careers_usecase = GetAllCareersUsecase(career_repository)
