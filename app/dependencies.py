import motor.motor_asyncio


MONGODB_URL = "mongodb://mongo_db:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.fastapi_project
collection = database.events


database = client["fastapi_project"]


# async def get_value(database):
#     collection = await database["events"].find().to_list(length=100)
